import boto.ec2, sys, time

runningInstance = []

def getConnectionInstance(instanceRegion):    
    try:        
        conn = boto.ec2.connect_to_region(instanceRegion,aws_access_key_id='',aws_secret_access_key='')
        return conn
    except:
        return None

def startInstance(noOfInstance,instanceRegion):
    aws = getConnectionInstance(instanceRegion)
    if not aws is None:        
        global runningInstance        
        try:
            print ('Initializing '+str(noOfInstance)+' EC2 instance(s) in '+instanceRegion+' region ...')
            for i in range(noOfInstance):
                reservation = aws.run_instances('ami-9ff7e8af',instance_type = 't2.micro')
                runningInstance.append(reservation.instances[0])
                print ('Initialized '+str(runningInstance[-1])+' State: '+runningInstance[-1].state)
        except:
            print (sys.exc_info()[1])
        while True:
            try:    
                task = int(input('Enter:\n1 to terminate all instance(s)\n2 to terminate a specific instance only\n0 to exit\n'))    
                if task == 0:
                    sys.exit(0)
                elif task == 1:
                    stopInstance(noOfInstance,'us-west-2')        
                elif task == 2:
                    terminationId = input('Enter instacnce ID: ')
                    stopInstance(noOfInstance,'us-west-2',terminationId)
                    time.sleep(2)
                else:
                    raise ValueError
            except ValueError as e:
                print ('Invalid value provided')
                continue    
            except:
                print (sys.exc_info()[1])
            break        
    else:
        print ('Error establishing connection to AWS')
        sys.exit(0)
        
def stopInstance(noOfInstance,instanceRegion,*args):
    global runningInstance      
    if len(args) == 0:
        try:
            print ('Initializing termination sequence for running instance(s) ...')
            for instance in runningInstance:
                print ('Terminating '+str(instance))
                instance.terminate()                
                time.sleep(2)
        except:
            print (sys.exc_info()[1])            
    else:
        try:           
            x = 0
            aws = getConnectionInstance(instanceRegion)
            for arg in args:
                if arg == 'stop':
                    reservations = aws.get_all_reservations()                           
                    for reservation in reservations:
                        if reservation.instances[0].state == 'running' or reservation.instances[0].state == 'pending':
                            try:
                                print ('Terminating '+str(reservation.instances[0]))
                                reservation.instances[0].terminate()
                                x += 1
                            except:
                                print (sys.exc_info()[1])                        
                    if x == 0:
                        print ('Not enough instances available')
                else:                    
                    print ('Initiating termination sequence for Instance:'+str(arg))
                    aws.terminate_instances(instance_ids=[arg])        
                    print ('Instance terminated')
        except:
            print (sys.exc_info()[1])





noOfInstance = int(sys.argv[1])
instanceRegion = sys.argv[2]
activity = sys.argv[3]

if activity == "start":
    startInstance(noOfInstance, instanceRegion)
elif activity == "stop":
    stopInstance(noOfInstance,instanceRegion,activity)