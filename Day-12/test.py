def update_server_config(file_path, key, value):
    #read the existing content of server config file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    #update the config value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            #check if the line starts with the specified key value
            if key in line:
                #update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                #keep the existing line as it is
                file.write(line)
#path to the server config file
server_config_file = 'server.conf'
#key and new value for updating the server confugurations
key_to_update = 'MAX_CONNECTIONS'
new_value = '800' #new maximum connections allowed

#update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)