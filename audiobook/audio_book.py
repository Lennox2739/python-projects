import PyPDF2
import pyttsx3
from pathlib import Path

class AudioBookConverter:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
    
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file."""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text: {e}")
            return None
    
    def convert_to_audio(self, text, output_file, speed=150, voice_id=0):
        """Convert text to audio file."""
        try:
            self.engine.setProperty('rate', speed)
            if voice_id < len(self.voices):
                self.engine.setProperty('voice', self.voices[voice_id].id)
            
            self.engine.save_to_file(text, output_file)
            self.engine.runAndWait()
            print(f"Audio saved to: {output_file}")
        except Exception as e:
            print(f"Error converting to audio: {e}")
    
    def convert_pdf_to_audiobook(self, pdf_path, speed=150, voice_id=0):
        """Main method to convert PDF to audiobook."""
        print(f"Processing: {pdf_path}")
        text = self.extract_text_from_pdf(pdf_path)
        if text:
            pdf_name = Path(pdf_path).stem
            output_file = f"{pdf_name}_audiobook.mp3"
            self.convert_to_audio(text, output_file, speed, voice_id)
            return output_file
        return None

if __name__ == "__main__":
    converter = AudioBookConverter()
    # Example usage
    pdf_file = input("Enter PDF file path: ")
    speed = int(input("Enter speed (50-300, default 150): ") or 150)
    voice_id = int(input("Enter voice ID (0 or 1): ") or 0)
    converter.convert_pdf_to_audiobook(pdf_file, speed, voice_id)
