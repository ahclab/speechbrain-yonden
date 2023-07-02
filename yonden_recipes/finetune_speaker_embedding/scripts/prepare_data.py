from argparse import ArgumentParser
from tqdm import tqdm
from pathlib import Path
import soundfile as sf
import csv


def main():
    parser = ArgumentParser()
    parser.add_argument("--input-file", type=Path, required=True, help="file path of yonden spk to wavfile data")
    parser.add_argument("--output-file", type=Path, required=True, help="file path of output data")
    args = parser.parse_args()
    
    csv_output = [["ID", "duration", "wav", "start", "stop", "spk_id"]]
    known_speakers = []
    
    with open(args.input_file, "r", encoding="utf-8") as input_file:
        for i, line in enumerate(tqdm(input_file.readlines())):
            # preprocessing
            line = line.strip()
            if line == "":
                continue
            line = line.split(" ")
            
            # get information
            spk_name = line[0]
            if spk_name in known_speakers:
                spk_id = known_speakers.index(spk_name)
            else:
                spk_id = len(known_speakers)
                known_speakers.append(spk_name)
            
            wav_path = line[1]
            wav, sr = sf.read(wav_path)
            duration = len(wav) / sr
            start = 0
            stop = wav.shape[0] - 1
            
            # append to csv_output
            csv_output.append([i, duration, wav_path, start, stop, spk_id])
    
    # write csv_output
    with open(args.output_file, "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(csv_output)


if __name__ == '__main__':
    main()