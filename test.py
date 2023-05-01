# @app.route("/users/<int:id>", methods=["GET"])
# def get_users(id):
#     try :
#         with threadLock:
#             if(id <= 0):
#                 return {'err': 'bad request'},400
#             else:
#                 user = find_users(id)
#                 if user == None:
#                     return {'err': 'not found'},404 
#                 else:
#                     if(isinstance(user['id'], int)): #check for the date is remaining
#                         return {'id': user['id'],'username' : user['username'], 'email' : user['email address'], 'timestamp': user['timestamp'], 'posts' : user['posts']}, 200
#     except Exception as e:
#         return {'err': 'bad request'},400

# @app.route("/users/<int:id>/delete/<string:key>", methods=['DELETE'])
# def delete_user(id,key):
#     try :
#         with threadLock:
#             if(id <= 0):
#                 return {'err': 'bad request'},400
#             else:
#                 user = find_users(id)
#                 if user == None:
#                     return {'err': 'not found'},404
#                 elif(user['key'] != key):
#                     return {'err': 'forbidden'},403
#                 else:
#                     users.remove(user)
#                     return user,200
#     except Exception as e:
#         return {'err': 'bad request'},400

# @app.route("/users/<int:id>/posts", methods=['POST'])
# def create_post(id):
#     try :
#         with threadLock:
#             if(id <= 0):
#                 return {'err': 'bad request'},400
#             else:
#                 user = find_users(id)
#                 if user == None:
#                     return {'err': 'not found'},404
#                 else:
#                     data = request.get_json()
#                     if(data == None):
#                         return {'err': 'bad request'},400
                    
#                     elif ('msg' not in data or  not isinstance(data['msg'],str)):
#                         return {'err': 'bad request'},400
                    
#                     elif(not isinstance(data['msg'],str)):
#                         return {'err': 'bad request'},400
                    
#                     else:  
#                         msg = data['msg']
#                         id = postId + 1
#                         # id = len(posts)+1 
#                         # To be implement : can also declare a id as a global variable and then keep on adding one when we create the post this can be used to avoid the repeating ids.

#                         key = secrets.token_hex(15)
#                         timestamp = datetime.now().utcnow().isoformat()

#                         posts_data = {'id': id, 'key': key, 'msg' : msg, 'timestamp': timestamp}
#                         posts.append(posts_data)
#                         user['posts'].append(posts_data)
#                         print(posts)
#                         return posts_data, 200
#     except Exception as e:
#         return {'err': 'bad request'},400