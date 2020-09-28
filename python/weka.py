from os import listdir
from os.path import isfile, join
from read_image import ReadImage
from logger import Logger


class Weka():
    def __init__(self, images_directory):
        self.images_directory = images_directory
        self.header = '''@relation caracteristicas\n
                         @attribute azul_cabelo_milhouse real
                         @attribute rosa_camisa_milhouse real
                         @attribute vermelho_shorts_milhouse real
                         @attribute marrom_pele_apu real
                         @attribute amarelo_calca_apu real
                         @attribute verde_jaqueta_apu real
                         @attribute classe {Milhouse, Apu}\n
                         @data\n
                      '''
        self.body = ''

    def list_directory_files(self):
        Logger.log('Reading all folder files')
        onlyfiles = [f for f in listdir(self.images_directory) if isfile(
            join(self.images_directory, f))]
        Logger.log(
            f'\n{len(onlyfiles)} images found in {self.images_directory} directory!', True)

        # Range with 5 images for testing
        return onlyfiles

    def extractTo(self, fileName):
        output_filename = fileName + '.arff'
        imagesData = []

        for index, image in enumerate(list(self.list_directory_files())):
            Logger.log(f'Extracting characteristics from {image}')

            features = ReadImage().read(f'{self.images_directory}/{image}')
            features[6] = "Milhouse" if features[6] == 0.0 else "Apu"
            imagesData.append(features)

            Logger.log(f'Data added to index {index}')
            Logger.log('Extracted Features:')
            Logger.log(f'Milhouse Blue Hair = {features[0]}')
            Logger.log(f'Milhouse Pink Shirt = {features[1]}')
            Logger.log(f'Milhouse Red Shorts = {features[2]}')
            Logger.log(f'Apu Brown Skin = {features[3]}')
            Logger.log(f'Apu Green Jacket = {features[4]}')
            Logger.log(f'Apu Yellow Pants = {features[5]}')
            Logger.log(f'Class = {features[6]}', True)

            self.body += ','.join(map(str, features)) + "\n"

        Logger.log(f'Writing the ARFF file {output_filename} to disk')
        with open(output_filename, 'w') as fp:
            fp.write(self.header)
            fp.write(self.body)

        Logger.log('All Done!')
        return imagesData
