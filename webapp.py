import random
import streamlit as st
import re, os
from docx import Document
from globals import writer


def sanitize_filename(filename):
    # Split the filename into the base name and extension
    base_name, extension = os.path.splitext(filename)
    
    # Remove any characters that are not letters, numbers, underscores, or spaces from the base name
    sanitized_base_name = re.sub(r'[^a-zA-Z0-9_ ]', '', base_name)
    # Replace spaces with underscores in the base name
    sanitized_base_name = sanitized_base_name.replace(' ', '_')
    
    # Combine the sanitized base name and the original extension
    sanitized_filename = sanitized_base_name + extension
    
    return sanitized_filename


def main():
    st.title("Document Processing App")
    
    words = st.text_input("Words to output")
    rules = st.text_area("Rules")
    
    if not words:
        st.write("Word limit is required")
    else:
        document_file = st.file_uploader("Upload Document")
        if document_file is not None and words and rules:
            save_folder = "files"
            output_folder = "output"        
            
            os.makedirs(save_folder, exist_ok=True)
            os.makedirs(output_folder, exist_ok=True)
            
            sanitized_filename = sanitize_filename(document_file.name)
            infile_path = os.path.join(save_folder, sanitized_filename)
            outfile_path = os.path.join(output_folder, sanitized_filename)

            st.success("Document saved successfully!")
            if os.path.exists(infile_path):
                os.remove(infile_path)
                
            with open(infile_path, mode='wb') as w:
                w.write(document_file.getvalue())        
                
            output = writer.run(infile_path, outfile_path, random.randrange(0,1), 1500, words, rules)
            
            st.success("Document processed and output saved successfully!")
            st.subheader("Download Processed File:")
            
            st.download_button("Download", data=open(outfile_path, 'rb'), file_name=sanitized_filename)
            
            st.subheader("Processed Output:")
            st.write(output)

if __name__ == "__main__":
    main()
