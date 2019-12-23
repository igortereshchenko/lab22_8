import plotly
import plotly.graph_objs as go
import json

from flask import render_template, flash, request, redirect, session
from ORM import *
from WTForms import *

app.secret_key = 'development key'



#lab 2 part =====================


@app.route('/show', methods=['GET', 'POST'])
def show():

    form = HostForm()
    select_result = Host.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_row = Host.query.filter_by(hostname=selected_pk_data).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('show.html', data=select_result, form=form)

    return render_template('show.html', data=select_result, form=form)


@app.route('/insert', methods=['GET', 'POST'])
def insert():

    form = HostForm()
    select_result = Host.query.filter_by().all()

    if request.method == 'POST':
        print(form.validate()),
        if not form.validate():
            flash('All fields are required.')
            return render_template('insert.html', data=select_result, form=form)
        else:
            host = Host(form.hostname.data, form.price.data, form.speed.data, form.os_type.data)
            db.session.add(host)
            db.session.commit()
            select_result.append(host)

    return render_template('insert.html', data=select_result, form=form)



@app.route('/get', methods=['GET', 'POST'])
def get():

    data = [{"hostname": "test21", "price": 234444, "speed": 7, "os_type": "Linux"},
            {"hostname": "test22", "price": 165487, "speed": 5, "os_type": "Microsoft"},
            {"hostname": "test23", "price": 854124, "speed": 1, "os_type": "Linux"}]

    form = HostForm()
    select_result = Host.query.filter_by().all()

    if request.method == 'GET':
        for row in data:
            host = Host(row["hostname"], row["price"], row["speed"], row["os_type"])
            db.session.add(host)
        db.session.commit()
        select_result.append(host)

    return redirect("/show")


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    data = Host.query\
        .filter_by().order_by(Host.hostname).all()
    hostname_list = []
    speed_list = []
    for i in range(len(data)):
        hostname_list.append(data[i].hostname)
        speed_list.append(data[i].speed)
    

    #Pie chart
    '''trace = go.Pie(
        labels=hostname_list,
        values=speed_list
    )'''
    #Scatter chart
    '''trace = go.Scatter(
        x=hostname_list,
        y=speed_list
    )'''
    #Bar chart
    trace = go.Bar(
    x=hostname_list, 
    y=speed_list
    )
    
    data_to_plot = [trace]
    graphJSON = json.dumps(data_to_plot, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('shop.html', graphJSON=graphJSON)

#End lab 2 part =================




@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/edit_users', methods = ['GET', 'POST'])
def edit_users():

    form = UsersForm()
    select_result = Users.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('users.html', data=select_result, form=form)
        else:
            nickname = session['users_edit_pk_data']
            user = Users.query.filter_by(nickname=nickname).first()
            user.nickname = form.nickname.data
            user.login = form.login.data
            user.password = form.password.data
            db.session.commit()
            return render_template("users.html", data=select_result, form=form)

    return render_template("users.html", data=select_result, form=form)


@app.route('/users', methods=['GET', 'POST'])
def users():

    form = UsersForm()
    select_result = Users.query.filter_by().all()

    if request.method == 'POST':

        selected_nickname = request.form.get('del')
        if selected_nickname is not None:
            selected_row = Users.query.filter_by(nickname=selected_nickname).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('users.html', data=select_result, form=form)

        selected_nickname = request.form.get('edit')
        if selected_nickname is not None:
            selected_row = Users.query.filter_by(nickname=selected_nickname).first()
            session['users_edit_pk_data'] = selected_nickname
            return render_template("edit_users.html", row=selected_row, form=form)

        print(form.validate()),
        if not form.validate():
            flash('All fields are required.')
            return render_template('users.html', data=select_result, form=form)
        else:
            user = Users(form.nickname.data, form.login.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            select_result.append(user)

    return render_template('users.html', data=select_result, form=form)


@app.route('/edit_sites', methods=['GET', 'POST'])
def edit_sites():

    form = SitesForm()
    select_result = Sites.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('sites.html', data=select_result, form=form)
        else:
            site_adress = session['sites_edit_pk_data']
            site = Sites.query.filter_by(site_adress=site_adress).first()
            site.site_adress = form.site_adress.data
            site.site_name = form.site_name.data
            print(site.site_name)
            db.session.commit()
            return render_template("sites.html", data=select_result, form=form)

    return render_template("sites.html", data=select_result, form=form)


@app.route('/sites', methods=['GET', 'POST'])
def sites():

    form = SitesForm()
    select_result = Sites.query.filter_by().all()

    if request.method == 'POST':

        selected_site_adress = request.form.get('del')
        if selected_site_adress is not None:
            selected_row = Sites.query.filter_by(site_adress=selected_site_adress).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('sites.html', data=select_result, form=form)

        selected_site_adress = request.form.get('edit')
        if selected_site_adress is not None:
            selected_row = Sites.query.filter_by(site_adress=selected_site_adress).first()
            session['sites_edit_pk_data'] = selected_site_adress
            return render_template("edit_sites.html", row=selected_row, form=form)

        print(form.validate()),
        if not form.validate():
            flash('All fields are required.')
            return render_template('sites.html', data=select_result, form=form)
        else:
            site = Sites(form.site_adress.data, form.site_name.data)
            db.session.add(site)
            db.session.commit()
            select_result.append(site)

    return render_template('sites.html', data=select_result, form=form)


@app.route('/edit_styles', methods=['GET', 'POST'])
def edit_styles():

    form = StylesForm()
    select_result = Styles.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('styles.html', data=select_result, form=form)
        else:
            style_name = session['styles_edit_pk_data']
            style = Styles.query.filter_by(style_name=style_name).first()
            style.style_name = form.style_name.data
            style.code = form.code.data
            style.premium = form.premium.data
            db.session.commit()
            return render_template("styles.html", data=select_result, form=form)

    return render_template("styles.html", data=select_result, form=form)


@app.route('/styles', methods=['GET', 'POST'])
def styles():

    form = StylesForm()
    select_result = Styles.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data
            selected_row = Styles.query.filter_by(style_name=selected_pk_data).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('styles.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data
            selected_row = Styles.query.filter_by(style_name=selected_pk_data).first()
            session['styles_edit_pk_data'] = selected_pk_data
            return render_template("edit_styles.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('styles.html', data=select_result, form=form)
        else:
            style = Styles(form.style_name.data, form.code.data, form.premium.data)
            db.session.add(style)
            db.session.commit()
            select_result.append(style)

    return render_template('styles.html', data=select_result, form=form)




@app.route('/edit_topicanalitycs', methods=['GET', 'POST'])
def edit_topicanalitycs():

    form = TopicAnalitycsForm()
    select_result = TopicAnalitycs.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('topicanalitycs.html', data=select_result, form=form)
        else:
            topic_name = session['topicanalitycs_edit_pk_data']
            topic = TopicAnalitycs.query.filter_by(topic_name=topic_name).first()

            topic.topic_name = form.topic_name.data
            topic.words = form.words.data
            topic.paragraphs = form.paragraphs.data
            topic.focus_time = form.focus_time.data
            topic.sentences = form.sentences.data
            topic.images = form.images.data

            db.session.commit()
            return render_template("topicanalitycs.html", data=select_result, form=form)

    return render_template("topicanalitycs.html", data=select_result, form=form)


@app.route('/topicanalitycs', methods=['GET', 'POST'])
def topicanalitycs():

    form = TopicAnalitycsForm()
    select_result = TopicAnalitycs.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data
            selected_row = TopicAnalitycs.query.filter_by(topic_name=selected_pk_data).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('topicanalitycs.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data
            selected_row = TopicAnalitycs.query.filter_by(topic_name=selected_pk_data).first()
            session['topicanalitycs_edit_pk_data'] = selected_pk_data
            return render_template("edit_topicanalitycs.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('topicanalitycs.html', data=select_result, form=form)
        else:
            topic = TopicAnalitycs(form.topic_name.data, form.words.data, form.paragraphs.data, form.focus_time.data, form.sentences.data, form.images.data)
            db.session.add(topic)
            db.session.commit()
            select_result.append(topic)

    return render_template('topicanalitycs.html', data=select_result, form=form)

@app.route('/edit_block', methods=['GET', 'POST'])
def edit_block():

    form = BlockForm()
    select_result = Block.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('block.html', data=select_result, form=form)
        else:
            selected_block_pk_data_list = session['block_edit_pk_data'].split("█")
            selected_style_name = selected_block_pk_data_list[0]
            selected_block_name = selected_block_pk_data_list[1]
            selected_block_type = selected_block_pk_data_list[2]
            block = Block.query.filter_by(style_name=selected_style_name, block_name = selected_block_name, block_type = selected_block_type).first()

            block.style_name = form.style_name.data
            block.block_name = form.block_name.data
            block.block_type = form.block_type.data
            block.code = form.code.data
            block.source = form.source.data

            db.session.commit()
            return render_template("topicanalitycs.html", data=select_result, form=form)

    return render_template("block.html", data=select_result, form=form)


@app.route('/block', methods=['GET', 'POST'])
def block():

    form = BlockForm()
    select_result = Block.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_style_name = selected_pk_data[0]
            selected_block_name = selected_pk_data[1]
            selected_block_type = selected_pk_data[2]
            selected_row = Block.query.filter_by(style_name=selected_style_name, block_name = selected_block_name, block_type = selected_block_type).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            session['block_edit_pk_data'] = selected_pk_data
            return render_template('block.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_style_name = selected_pk_data[0]
            selected_block_name = selected_pk_data[1]
            selected_block_type = selected_pk_data[2]
            selected_row = Block.query.filter_by(style_name=selected_style_name, block_name = selected_block_name, block_type = selected_block_type).first()
            session['block_edit_pk_data'] = selected_pk_data
            return render_template("edit_block.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('block.html', data=select_result, form=form)
        else:
            block = Block(form.style_name.data, form.block_name.data, form.block_type.data, form.code.data, form.source.data)
            db.session.add(block)
            db.session.commit()
            select_result.append(block)

    return render_template('block.html', data=select_result, form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = DashboardForm()
    if request.method == 'POST':
        hostname = form.hostname.data
        price = form.price.data
    else:
        hostname = 'gogle123'
        price = '23113.0'
    data = Server.query\
        .filter_by().order_by(Server.hostname).all()
    hostname_list = []
    price_list = []
    for i in range(len(data)):
        hostname_list.append(data[i].hostname)
        price_list.append(data[i].price)


if __name__ == '__main__':
    app.run(debug=True)