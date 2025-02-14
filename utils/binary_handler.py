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

    def read_all_content(self, mode="十六进制"):
        """读取并显示整个文件内容"""
        return self.read_content(0, len(self.content), mode)
    
    def convert_base(self, data, from_base="二进制", to_base="十六进制"):
        """在不同进制间转换"""
        bases = {
            "二进制": 2,
            "八进制": 8,
            "十进制": 10,
            "十六进制": 16
        }
        
        # 先转换为十进制
        if from_base == "ASCII":
            decimal = ord(data) if isinstance(data, str) else data
        else:
            decimal = int(str(data), bases[from_base])
        
        # 转换为目标进制
        if to_base == "ASCII":
            return chr(decimal)
        elif to_base == "二进制":
            return bin(decimal)[2:]
        elif to_base == "八进制":
            return oct(decimal)[2:]
        elif to_base == "十六进制":
            return hex(decimal)[2:]
        else:  # 十进制
            return str(decimal)

    def _format_hex(self, data):
        hex_view = []
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            hex_line = ' '.join([f'{b:02x}' for b in chunk])
            ascii_part = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in chunk])
            # 添加ASCII对照
            hex_view.append(f'{i:08x}: {hex_line:<48} |{ascii_part}|')
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
        for i in range(0, len(data), 4):  # 每行显示4个字节
            chunk = data[i:i+4]
            binary_line = ' '.join([f'{b:08b}' for b in chunk])
            hex_part = ' '.join([f'{b:02x}' for b in chunk])
            # 添加十六进制对照
            binary_view.append(f'{i:08x}: {binary_line:<35} |{hex_part}|')
        return '\n'.join(binary_view)
