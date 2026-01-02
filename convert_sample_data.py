import os
import numpy as np
import pandas as pd

# Enter the sampling rate in ECG
FS = 512                    
DTYPE = np.int16            
SKIP_SECONDS = 60           #skipping the first 10 second of the ECG file
DURATION_SECONDS = 1200      


# This finds the directory where THIS script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script location
INPUT_DIR = os.path.join(BASE_DIR, 'Data', 'ECG-Raw')
OUTPUT_FILE = os.path.join(BASE_DIR, 'Data', 'sample_ecg.csv')

def main():
    # Ensure Output Directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory not found at {INPUT_DIR}")
        print("Please create 'Data/ECG-Raw' and place .bin files there.")
        return

    bin_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.bin')]
    if not bin_files:
        print(f"Error: No .bin files found in {INPUT_DIR}")
        return

    target_file = os.path.join(INPUT_DIR, bin_files[0])
    print(f"Processing: {target_file}")

    try:
        # 1. Load Raw Data (Honest Data - ADC Units)
        raw_data = np.fromfile(target_file, dtype=DTYPE)
        
        # 2. Slice Data
        start_idx = SKIP_SECONDS * FS
        end_idx = start_idx + (DURATION_SECONDS * FS)

        if len(raw_data) < end_idx:
            segment = raw_data[start_idx:]
            print("Warning: Requested duration exceeds file length. Using available data.")
        else:
            segment = raw_data[start_idx:end_idx]

        # 3. Save to CSV
        df = pd.DataFrame({'ECG': segment})
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Success! Converted data saved to: {OUTPUT_FILE}")
        print(f"Signal shape: {df.shape}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()