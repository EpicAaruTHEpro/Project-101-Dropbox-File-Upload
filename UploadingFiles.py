import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to): 
        dbx= dropbox.Dropbox(self.access_token)
        with open(file_from , 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        
def upload():
    access_token = input("Please input your access code of dropbox: ")
    transferData = TransferData(access_token)

    file_from = input("What file do you want: ")
    file_to = input("Where do you want the file in dropbox: ")

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    upload()
