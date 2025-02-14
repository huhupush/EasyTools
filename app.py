import streamlit as st
from utils.binary_handler import BinaryHandler
import os

def main():
    st.title("二进制文件查看器")
    
    # 文件上传
    uploaded_file = st.file_uploader("选择二进制文件", type=None)
    
    if uploaded_file is not None:
        # 创建 BinaryHandler 实例
        handler = BinaryHandler(uploaded_file)
        
        # 显示文件基本信息
        st.write("文件名:", uploaded_file.name)
        st.write("文件大小:", handler.get_file_size(), "bytes")
        
        # 选择查看模式
        view_mode = st.selectbox(
            "选择查看模式",
            ["十六进制", "ASCII", "二进制"]
        )
        
        # 显示文件内容
        chunk_size = st.slider("选择每次显示的字节数", 16, 256, 64)
        offset = st.number_input("起始偏移量", min_value=0, value=0)
        
        content = handler.read_content(offset, chunk_size, view_mode)
        st.text_area("文件内容", content, height=300)

if __name__ == "__main__":
    main()
