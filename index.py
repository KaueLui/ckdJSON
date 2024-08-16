import os
import glob
import json

def organize_json(input_path, output_path):
    
    # Carregar o arquivo JSON
    # Load the JSON file
    with open(input_path, 'r') as file:
        json_data = json.load(file)
    
    # Organizar o JSON
    # Organize the JSON
    organized_json = json.dumps(json_data, indent=4)

    # Salvar o JSON em um novo arquivo
    # Save the JSON in a new file

    with open(output_path, 'w') as file:
        file.write(organized_json)

    # Confirmação no CMD que o JSON foi organizado.
    # Confirmation in CMD that the JSON has been organized.
    print(f"JSON organizado salvo em: {output_path}")

def main():
    input_directory = 'input'
    output_directory = 'output'
    os.makedirs(output_directory, exist_ok=True)
    
    #Define as extensões que serão buscadas para organizar
    # Define the extensions to be searched for organization
    extensions = ['.ktape.ckd', '.dtape.ckd', '.tpl.ckd', '.tape.ckd']
    
    #Processamento dos arquivos
    # Processing the files
    for extension in extensions:
        pattern = os.path.join(input_directory, f'*{extension}')
        files = glob.glob(pattern)
        
    #Obtendo o nome do arquivo base.
    # Obtaining the base filename  
        for file in files:
            filename = os.path.basename(file)
            output_file_path = os.path.join(output_directory, f'{filename}_organized.json')

    #Chamando função para organizar o arquivo.
    # Calling function to organize the file
            organize_json(file, output_file_path)

    #Execução
    # Execution
if __name__ == "__main__":
    main()
