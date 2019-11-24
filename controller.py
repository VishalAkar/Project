import web
from PIL import Image
import Models.model as model
import os


web.config.debug = False

urls = (
    '/','Home',
    '/upload-image/(.*)','upload',
    '/freshapples','FreshApples'
)

app = web.application(urls,globals())

session = web.session.Session(app,web.session.DiskStore("sessions"), initializer={'user':'none'})

session_data = session._initializer

render = web.template.render("Views/Tempelates",globals={'session':session_data,'current_user':session_data['user']})






#Classes/Routes

class Home:
    def GET(self):
        return render.index()
    def POST(self):
        data = web.input()
        print(data.keys())
    """
        s=str(data.keys())
        s = s[12:]
        s=s[0:len(s)-3]
        u = upload()
        s=u.filepath
        print(s)
        mod = model.model1()
        res=mod.webmodel(s)
        return res"""
      
class upload:
    print("upload called")
    def POST(self,type):
        print("Post is called")
        file = web.input()
        file_dir = os.getcwd()+"/static/upload"
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        filepath = file_dir+"/"+"apple.jpg"
        f =open(filepath,'wb')
        f.write(file['img'])
        f.close()
        print(filepath)
        mod = model.model1()
        res=mod.webmodel(filepath)
        a = str(res)
        print(a)
        if(a=='freshapples'):
            return web.redirect('/freshapples')
        else:
            return res

class FreshApples:
    def GET(self):
        return render.apple()

'''
class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()
        print(data)
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

class Database:
    def GET(self):
        return render.Database()
    
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.imageUpload(data)

class Login:
    def GET(self):
        return render.Login()

    def POST(self):
        data = web.input()
        print(data)
        reg_model = RegisterModel.RegisterModel()
        flag = reg_model.isUser(data)
        if flag == True:
            return web.redirect('/database','303')
        else:
            print("You are not authorized")
            '''

if __name__ =="__main__":
    app.run()   