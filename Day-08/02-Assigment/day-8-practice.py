servers = ['web_01_server', 'app_01_server', 'db_01_server']
servers.append('web_02-server')
servers.remove('web_01_server')
servers.append('web_01-server')

subset = servers[0:3]
print(subset)

my_tuple = ('prav_demo_bucket', 'vamsi_demo_bucket', 'eeshu_demo_bucket', 'sreeshu_demo_bucket') 
is_present = 'vamsi_demo_bucket' in my_tuple

#print(is_present, 'vamsi_demo_bucket is present in tuple list')
new_tuple = my_tuple + ('valli', 'krithik')
