class BinaryHandler:
    def __init__(self, file):
        self.file = file
        self.content = file.read()
    
    def get_file_size(self):
        return len(self.content)
    
    def read_content(self, offset, length, mode):
        chunk = self.content[offset:offset+length]
        
        if mode == "十六进制":
            return self._format_hex(chunk)
        elif mode == "ASCII":
            return self._format_ascii(chunk)
        else:  # 二进制
            return self._format_binary(chunk)
    
    def _format_hex(self, data):
        hex_view = []
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            hex_line = ' '.join([f'{b:02x}' for b in chunk])
            hex_view.append(f'{i:08x}: {hex_line}')
        return '\n'.join(hex_view)
    
    def _format_ascii(self, data):
        ascii_view = []
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            ascii_line = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in chunk])
            ascii_view.append(f'{i:08x}: {ascii_line}')
        return '\n'.join(ascii_view)
    
    def _format_binary(self, data):
        binary_view = []
        for i in range(0, len(data), 8):
            chunk = data[i:i+8]
            binary_line = ' '.join([f'{b:08b}' for b in chunk])
            binary_view.append(f'{i:08x}: {binary_line}')
        return '\n'.join(binary_view)
