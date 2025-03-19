# Text Encoding and Decoding Project

This project implements an original text encoding and decoding method using a dynamic character padding approach. The method provides a unique way to transform text while maintaining its readability and security.

## Overview

The encoding method works by adding random characters after each character of the original text, following a specific pattern defined by a key. This creates an encoded text that appears random but can be decoded using the same key.

## Features

- Dynamic character padding based on a key sequence
- Support for extended ASCII characters
- Random character generation for padding
- Key-based encoding and decoding
- File-based input/output operations

## How It Works

### Encoding Process

1. The system uses a predefined alphabet containing various characters (ASCII and extended ASCII)
2. A key is randomly selected from a key file (`cles.txt`)
3. For each character in the input text:
   - The character is kept as is
   - A number of random characters (defined by the key) are added after it
4. The key number is written at the beginning of the encoded file

### Decoding Process

1. The system reads the key number from the encoded file
2. Retrieves the corresponding key from the key file
3. For each character in the encoded text:
   - Keeps the first character (original character)
   - Skips the number of padding characters defined by the key
4. Reconstructs the original text

## File Structure

- `codage_texte.py`: Contains the encoding logic
- `decodage_texte.py`: Contains the decoding logic
- `cles.txt`: Contains the encoding keys
- `albatros.txt`: Input text file
- `albatros_chiffre.txt`: Encoded text output
- `albatros_dechiffre.txt`: Decoded text output

## Usage

1. Place your input text in `albatros.txt`
2. Run the encoding script:
   ```bash
   python codage_texte.py
   ```
3. The encoded text will be saved in `albatros_chiffre.txt`
4. To decode, run:
   ```bash
   python decodage_texte.py
   ```
5. The decoded text will be saved in `albatros_dechiffre.txt`

## Key File Format

The `cles.txt` file should contain keys in the following format:
```
1 2 3 4 5
2 1 4 3 2
3 4 2 1 3
```

Each line represents a different key, where:
- The first number is the key identifier
- The remaining numbers define the padding pattern

## Security Features

- Random key selection for each encoding
- Variable padding length for each character
- Support for a wide range of characters
- No pattern repetition in the encoded text

## Requirements

- Python 3.x
- No additional dependencies required

## Author

Created by Alaeddine Ben Rhouma 