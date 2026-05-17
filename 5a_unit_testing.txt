from EmotionDetection import emotion_detector
import json
import requests

def run_tests():
    # Define our test cases with the statement and the expected dominant emotion
    test_cases = [
        {
            "statement": "I am glad this happened",
            "expected": "joy",
            "mock_scores": {"anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.95, "sadness": 0.02}
        },
        {
            "statement": "I am really mad about this",
            "expected": "anger",
            "mock_scores": {"anger": 0.92, "disgust": 0.03, "fear": 0.02, "joy": 0.01, "sadness": 0.02}
        },
        {
            "statement": "I feel disgusted just hearing about this",
            "expected": "disgust",
            "mock_scores": {"anger": 0.05, "disgust": 0.89, "fear": 0.02, "joy": 0.01, "sadness": 0.03}
        },
        {
            "statement": "I am so sad about this",
            "expected": "sadness",
            "mock_scores": {"anger": 0.02, "disgust": 0.02, "fear": 0.05, "joy": 0.01, "sadness": 0.90}
        },
        {
            "statement": "I am really afraid that this will happen",
            "expected": "fear",
            "mock_scores": {"anger": 0.02, "disgust": 0.01, "fear": 0.94, "joy": 0.01, "sadness": 0.02}
        }
    ]

    print("=== Running EmotionDetection Package Tests ===\n")
    
    passed_counts = 0

    for i, case in enumerate(test_cases, 1):
        # Format the mock scores into the nested JSON string structure your package expects
        mock_json_response = json.dumps({
            "emotionPredictions": [
                {
                    "emotion": case["mock_scores"],
                    "target": "",
                    "emotionMentions": [{"span": {"begin": 0, "end": len(case["statement"]), "text": case["statement"]}, "emotion": case["mock_scores"]}]
                }
            ],
            "producerId": {"name": "Mock Workflow", "version": "0.0.1"}
        })

        # Call the package function
        result = emotion_detector(mock_json_response)
        
        actual_dominant = result.get('dominant_emotion')
        
        # Verify the result
        if actual_dominant == case["expected"]:
            print(f"Test {i} PASSED")
            print(f"  Statement: \"{case['statement']}\"")
            print(f"  Result: Detected dominant emotion '{actual_dominant}' successfully.\n")
            passed_counts += 1
        else:
            print(f"Test {i} FAILED")
            print(f"  Statement: \"{case['statement']}\"")
            print(f"  Expected: {case['expected']}, Got: {actual_dominant}\n")

    print(f"=== Test Summary: {passed_counts}/{len(test_cases)} Passed ===")