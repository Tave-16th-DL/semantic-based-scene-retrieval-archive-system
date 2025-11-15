import os
import ffmpeg

input_folder = "data/split_scenes/clips_2"       
output_folder = "data/split_scenes/clips_2_audio_wav"  
os.makedirs(output_folder, exist_ok=True)

for file in sorted(os.listdir(input_folder)):
    if file.lower().endswith(".mp4"):
        in_path = os.path.join(input_folder, file)
        out_path = os.path.join(output_folder, file.replace(".mp4", ".wav"))

        (
            ffmpeg
            .input(in_path)
            .output(out_path, ac=1, ar=16000)  # mono, 16kHz
            .run(quiet=True)
        )

        print("음성 추출 완료 -", out_path)
