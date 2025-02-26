import os
import argparse

def replace_130B_to_130A(filename, flag=True):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if flag:
        lines[1] = "tech sky130A\n"
    else:
        lines[1] = "tech sky130B\n"
    
    with open(filename, 'w') as file:
        file.writelines(lines)
    
    print(f"Updated file: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace tech line in .mag files.')
    parser.add_argument('directory', type=str, help='Directory containing .mag files')
    parser.add_argument('--flag', type=str, choices=['True', 'False'], default='True', help='Flag to determine replacement (default: True)')
    
    args = parser.parse_args()
    flag = args.flag == 'True'
    print(f"Directory: {args.directory}")
    print(f"Flag: {flag}")

    for filename in os.listdir(args.directory):
        if filename.endswith('.mag'):
            replace_130B_to_130A(os.path.join(args.directory, filename), flag)