from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.moveRight()
for i in range(0,6):
    for move in range(6):
        if move == 6:
            robotArm.moveRight()
        else:
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
            robotArm.moveRight()
            


            
                


        
            



    
robotArm.wait()