from flask import Flask, jsonify, request
from colaborador import Colaborador

app = Flask(__name__)

name_list = [] 

@app.route('/get-users/<id>', methods = ['GET'])
def hello(id):
    user = request.args.get('user')    
    oData = []
    if user is None:
            oData = name_list
            print('Teste')
    else:
        for name in name_list:   
            if user == name['nome']:
                oData.append(name)
    return jsonify(oData), 200

@app.route('/create-user', methods = ['POST'])
def create_user():
    data = request.get_json()
    colabrador_dados = Colaborador(data['id'], data['departamento'], data['setor'], data['nome'], data['sobrenome'])
    name_list.append(colabrador_dados.dados_colaborador())    
    return jsonify(name_list), 201

@app.route('/delete-user', methods = ['DELETE'])
def delete_user():
    user_deleted = request.get_json()
    print(user_deleted['nome'])
    for name in name_list:
        if name['nome'] == user_deleted['nome']:
            name_list.remove(name)
            response = 'User deleted with success!'
        else:
            response = 'User not found!'             
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    

