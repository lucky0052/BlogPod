from flask import Flask,render_template,url_for
import os

app = Flask(__name__)


blogs = [
        { 'title':"Things are Crazy",
          'date': '19-12-2000',
          'user':'Lucky',
          'likes':'200',
          'link':'http://:www.google/lucky-blog',
          'content':'This is few lines by the author so just stop there.',
          'genre':'fantasy'
        },
        { 'title':"Things are the way they are.",
          'date': '19-12-2002',
          'user':'Karan',
          'likes':'300',
          'link':'http://:www.google/lucky-blog',
          'content':'This is another blogs so details should be different. So that it make a difference.',
          'genre':'intimidating'
        },
        { 'title':"Earth is Round",
          'date': '19-12-2004',
          'user':'Rohan',
          'likes':'100',
          'link':'http://:www.google/lucky-blog',
          'content':'This blog is about basically the reason behind the earth why it is round.',
          'genre':'Adventurous'
        },
        { 'title':"Things are Crazy",
          'date': '19-12-2000',
          'user':'Lucky',
          'likes':'200',
          'link':'http://:www.google/lucky-blog',
          'content':'This is few lines by the author so just stop there.',
          'genre':'fantasy'
        },
        { 'title':"Things are the way they are.",
          'date': '19-12-2002',
          'user':'Karan',
          'likes':'300',
          'link':'http://:www.google/lucky-blog',
          'content':'This is another blogs so details should be different. So that it make a difference.',
          'genre':'intimidating'
        }
        ,
        { 'title':"Earth is Round",
          'date': '19-12-2004',
          'user':'Rohan',
          'likes':'100',
          'link':'http://:www.google/lucky-blog',
          'content':'This blog is about basically the reason behind the earth why it is round.',
          'genre':'Adventurous'
        },
        { 'title':"Things are Crazy",
          'date': '19-12-2000',
          'user':'Lucky',
          'likes':'200',
          'link':'http://:www.google/lucky-blog',
          'content':'This is few lines by the author so just stop there.',
          'genre':'fantasy'
        },
        { 'title':"Things are the way they are.",
          'date': '19-12-2002',
          'user':'Karan',
          'likes':'300',
          'link':'http://:www.google/lucky-blog',
          'content':'This is another blogs so details should be different. So that it make a difference.',
          'genre':'intimidating'
        }
]
activities = [ {"time":'4:00 Pm',
              'title':'Earth is Round',
              'delete':'you have deleted titleName',
              'create':'you\'ve created a new podcast or blog.' 
             },

             {"time":'5:00 Pm',
              'title':'The Unknown World',
              'delete':'you have deleted titleName',
              'create':'you\'ve created a new podcast or blog.' 
             }

]

details = [
            { "que":"How to Upload the podcast and blogs?",
               "content": '''Accusantium dolore natus veniam quos aliquam repellat! 
                            Culpa dolorum facere vero voluptatibus consequuntur illo quidem quo rem! 
                            Officia eveniet sunt nisi obcaecati 
                           cumque voluptatum ad libero nulla laborum delectus culpa quod non! 
                           Perspiciatis nobis quos officia officiis molestias assumenda necessitatibus '''
                            
            },
            { "que":"How to Create an Account in BlogPod.",
               "content": '''Accusantium dolore natus veniam quos aliquam repellat! 
                            Culpa dolorum facere vero voluptatibus consequuntur illo quidem quo rem! 
                            Officia eveniet sunt nisi obcaecati 
                           cumque voluptatum ad libero nulla laborum delectus culpa quod non! 
                           Perspiciatis nobis quos officia officiis molestias assumenda necessitatibus '''
                            
            },
             { "que":"How to Submit a query or Bug?.",
               "content": '''Accusantium dolore natus veniam quos aliquam repellat! 
                            Culpa dolorum facere vero voluptatibus consequuntur illo quidem quo rem! 
                            Officia eveniet sunt nisi obcaecati 
                           cumque voluptatum ad libero nulla laborum delectus culpa quod non! 
                           Perspiciatis nobis quos officia officiis molestias assumenda necessitatibus '''
                            
            }

]

@app.route("/")
@app.route("/home")
def home():
   return render_template('logo.html', blogs = blogs)


@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route("/signup")
# def signup():
#     return render_template('index.html')

@app.route("/signin")
def signin():
    return render_template('signin1.html')

@app.route("/choice")
def choice():
    return render_template('choice.html')

@app.route('/dashboard')
def dashboard():
    return render_template('practice.html',title="Dashboard")

@app.route('/overview')
def profile():
    return render_template('profile.html',title="Profile")

@app.route('/blogs')
def blog():
    return render_template('blogs1.html',title="Blogs", blogs=blogs)

@app.route('/podcast')
def podcast():
    return render_template('podcast1.html',title=" Podcast")

@app.route('/upload')
def upload():
    return render_template('uploadchoice.html',title="Upload")

@app.route('/activity')
def activity():
    return render_template('activity.html',title="Your Activity", Activity = activities)

@app.route('/info')
def info():
    return render_template('info.html',title="Edit Information")

@app.route('/setting')
def setting():
    return render_template('settings.html',title="Update Details")

@app.route('/faq')
def faq():
    return render_template('faq.html',title="FAQ",details=details)

@app.route('/describe')
def describe():
    return render_template('describe.html',title="Account Setting")


@app.route('/top-podcast')
def topcast():
    return render_template('top.html',title="Top Podcast")


@app.route('/user/<name>')
def userpodcast(name):
    return render_template('userpage.html', title=f"{name}")


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    app.run(debug=True)
