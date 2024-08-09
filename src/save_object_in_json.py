from setting import OUTPUT_JSON
import json
import os



# Save object count data to JSON file

def save_object_counts(frame_numbers, filenames, num_objects):
    results = []
    for frame_number, filename, num_object in zip(frame_numbers, filenames, num_objects):
        results.append({
            'frame_number': frame_number,
            'image_name': filename,
            'number_of_objects': num_object
        })

    json_output_file = os.path.join(OUTPUT_JSON, 'object_counts.json')
    with open(json_output_file, 'w') as file:
        json.dump(results, file, indent=4)

    print(f"Object counts saved to {json_output_file}")