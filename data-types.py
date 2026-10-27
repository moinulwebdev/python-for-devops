#Datatypes
#Typecasting
#Concatenation
#Userinput



#String
# DevOps Example : storing cloud region, ip address, git branch name

cloud_regions = "us-east-1"
target_ip = "192.168.1.50"
git_branch = "main"



#Integer
#DevOps Example : Count active server instances, container replicas, network ports.

active_server_instances = 10
ssh_port = 22
max_retry_attempts = 3



#Float
#DevOps Example : CPU utilization, execution timers, system latency

cpu_utilization_percent = 80.5
api_response_latency_seconds = 0.014
disk_free_space_gb = 110.0



#List
#DevOps Example : A collection of server ips, microservice names, deployment stages.

server_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
deployment_stages = ["Build", "Test", "Deploy"]



#Dictionary
#DevOps Example : A configuration file or container specification

container_config = {
    "image" : "nginx:latest",
    "exposed_port" : 443,
    "environment" : "production",
    "is_healthy" : True
}

# print(server_ips)
# print(deployment_stages[-1])
# print(container_config["environment"])




#Type casting

x = str(10)
y = "30"

# print(x + y)

a = 20
b = float(30)

# print(a + b)




#Concatenation

# res = f"Cloud Region = " +cloud_regions + ' ' + "Target Ip = " +target_ip
# res = "Cloud Region = {}, Target Ip =  {}".format(cloud_regions,target_ip)




#User Input

username = input("Enter your username : ")
password = int(input("Enter your password : "))
# res = "Your username : {} \nYour password : {}".format(username,password)
# print(res)
print(username)
print(password)