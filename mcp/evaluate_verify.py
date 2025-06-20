#!/usr/bin/env python3
"""
Evaluation harness for the CAD verification MCP tool.

This script tests the cad_verify function against a set of test models
with known expected results to measure verification accuracy.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any

# Import the server module
import server


def load_expected_results() -> Dict[str, Any]:
    """Load expected results from JSON file."""
    results_file = Path(__file__).parent / "test_expected_results.json"
    if not results_file.exists():
        raise FileNotFoundError(f"Expected results file not found: {results_file}")
    
    with open(results_file, 'r') as f:
        return json.load(f)


def run_single_test(model_file: Path, expected_data: Dict[str, Any]) -> Dict[str, Any]:
    """Run verification on a single test model."""
    print(f"📝 Testing: {model_file.name}")
    
    # Run the verification
    result = server.cad_verify(str(model_file), expected_data["criteria"])
    
    # Check if result matches expectation
    actual_status = result["status"]
    expected_status = expected_data["expected"]
    
    is_correct = actual_status == expected_status
    
    print(f"   Expected: {expected_status}")
    print(f"   Actual:   {actual_status}")
    print(f"   Result:   {'✅ PASS' if is_correct else '❌ FAIL'}")
    
    if not is_correct:
        print(f"   Reason:   {expected_data['reason']}")
        print(f"   Details:  {result.get('details', 'N/A')}")
    
    return {
        "model": model_file.name,
        "expected": expected_status,
        "actual": actual_status,
        "correct": is_correct,
        "result": result
    }


def run_evaluation() -> Dict[str, Any]:
    """Run evaluation on all test models."""
    print("🚀 CAD Verification Evaluation Harness")
    print("=" * 50)
    
    # Load expected results
    try:
        expected_results = load_expected_results()
        print(f"📋 Loaded expectations for {len(expected_results)} models")
    except Exception as e:
        print(f"❌ Error loading expected results: {e}")
        return {"error": str(e)}
    
    # Find test models directory
    test_models_dir = Path(__file__).parent / "test_models"
    if not test_models_dir.exists():
        print(f"❌ Test models directory not found: {test_models_dir}")
        return {"error": f"Test models directory not found: {test_models_dir}"}
    
    # Run tests
    results = []
    correct_count = 0
    total_count = 0
    
    print("\n🧪 Running Tests:")
    print("-" * 30)
    
    for model_name, expected_data in expected_results.items():
        model_file = test_models_dir / model_name
        
        if not model_file.exists():
            print(f"⚠️  Model file not found: {model_name}")
            continue
        
        test_result = run_single_test(model_file, expected_data)
        results.append(test_result)
        
        if test_result["correct"]:
            correct_count += 1
        total_count += 1
        
        print()  # Empty line for readability
    
    # Calculate metrics
    accuracy = (correct_count / total_count * 100) if total_count > 0 else 0
    
    # Print summary
    print("📊 Evaluation Summary:")
    print("=" * 30)
    print(f"Total Tests:    {total_count}")
    print(f"Correct:        {correct_count}")
    print(f"Incorrect:      {total_count - correct_count}")
    print(f"Accuracy:       {accuracy:.1f}%")
    
    if accuracy == 100:
        print("🎉 Perfect score! All tests passed.")
    elif accuracy >= 80:
        print("✅ Good performance, minor issues to address.")
    else:
        print("⚠️  Significant issues detected, verification logic needs improvement.")
    
    return {
        "total_tests": total_count,
        "correct": correct_count,
        "accuracy": accuracy,
        "results": results
    }


def main():
    """Main function."""
    try:
        evaluation_results = run_evaluation()
        
        # Save detailed results
        results_file = Path(__file__).parent / "evaluation_results.json"
        with open(results_file, 'w') as f:
            json.dump(evaluation_results, f, indent=2)
        
        print(f"\n📄 Detailed results saved to: {results_file}")
        
        # Exit with appropriate code
        if evaluation_results.get("accuracy", 0) == 100:
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Evaluation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()