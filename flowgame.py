import pygame,sys,time,random
import numpy as np
from pygame.surfarray import array3d

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)

class FlowEnv:
    
    def __init__(self,frame_size,setpoint_x,setpoint_y,time_step):
        self.frame_size = frame_size
        self.game_window = pygame.display.set_mode((self.frame_size,self.frame_size))
        self.setpoint = [setpoint_x,setpoint_y]
        self.time_step = time_step
                
        #reset the game
        self.reset()
        
    def reset(self):
        self.game_window.fill(BLACK)
        self.droplet_pos = np.random.rand(2)
        #self.droplet_pos = np.array([0.2,0.1])
        
        self.Q1 = 0.5
        self.Q2 = - 0.5
        self.Q3 = 0.5
        self.step = 0
        self.action = None
        self.d_from_set_point = self.distance(self.setpoint,self.droplet_pos)
        (self.u,self.v) = self.calculate_drop_v(self.droplet_pos,self.Q1,self.Q2,self.Q3)
        print("GAME RESET")
        
    
    def human_step(self,event):
        '''
        Takes human keyboard event and then returns it as an action string
        '''
        
        action = None
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ################################################ 
        ########## CONVERT KEYPRESS TO DIRECTION ###### 
        ############################################## 
        elif event.type == pygame.KEYDOWN:
           #print('key_pressed')
           #print(event.key)            
            if event.key == pygame.K_g:
                action = '1up'
            if event.key == pygame.K_v:
                action = '1down'
            if event.key == pygame.K_h:
                action = '2up'
            if event.key == pygame.K_b:
                action = '2down'
            if event.key == pygame.K_j:
                action = '3up'
            if event.key == pygame.K_n:
                action = '3down'
            
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
        return action
        
    
    def change_flow_rates(self,action,Q1,Q2,Q3):
        
        if action=='1up':
            Q1 = Q1 + 0.05
            
        
        if action=='1down':
            Q1 = Q1 - 0.05
        
        if action=='2up':
            Q2 = Q2 + 0.05
            
        if action=='2down':
            Q2 = Q2 - 0.05
        
        if action=='3up':
            Q3 = Q3 + 0.05
            
            
        if action=='3down':
            Q3 = Q3 + 0.05
        
        return (Q1,Q2,Q3)
            
    def new_position (self,u,v,drop_pos,time_step):
        drop_pos[0] = drop_pos [0] + u*time_step
        drop_pos[1] = drop_pos [1] + v*time_step
        return drop_pos

      
    
    def distance(self,set_point,drop_pos):
        return np.linalg.norm(np.array(set_point)-np.array(drop_pos))
    
    def calculate_drop_v(self,drop_pos,Q1,Q2,Q3):
        psi1 = Q1
        psi2 = Q1+Q2
        psi3 = Q1+Q2+Q3
        u=psi2
        v=0
        for n in range (1,100):
            last_term = 2*np.cos(n*np.pi*drop_pos[1])/np.sinh(n*np.pi)
            last_term2 = 2*np.sin(n*np.pi*drop_pos[1])/np.sinh(n*np.pi)
            u = u + ((psi1+(psi2-psi1)*np.cos(n*np.pi))*np.sinh(n*np.pi*(1-drop_pos[0]))+(psi3+(psi2-psi3)*np.cos(n*np.pi))*np.sinh(n*np.pi*drop_pos[0]))*last_term
            v = v + ((psi1+(psi2-psi1)*np.cos(n*np.pi))*np.cosh(n*np.pi*(1-drop_pos[0]))-(psi3+(psi2-psi3)*np.cos(n*np.pi))*np.cosh(n*np.pi*drop_pos[0]))*last_term2
        
        
        return (u,v)
    
    
    
    def game_over(self):
        if self.droplet_pos [0] < 0.01 or self.droplet_pos[0] >0.99:
                self.end_game()
        if self.droplet_pos [1] < 0.01 or self.droplet_pos[1] > 0.99:
                self.end_game()
                
    def end_game(self):
        message = pygame.font.SysFont('arial', 45)
        message_surface = message.render('Game has Ended.', True, RED)
        message_rect = message_surface.get_rect()
        message_rect.midtop = (self.frame_size/2, self.frame_size/4)
        self.game_window.fill(BLACK)
        self.game_window.blit(message_surface, message_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
        
        


droplet_env = FlowEnv(600,0.5,0.5,0.05)
difficulty = 5
fps_controller = pygame.time.Clock()
check_errors = pygame.init()
pygame.display.set_caption('Droplet') 

while True:
    # Check Input from Human Step
    
    for event in pygame.event.get():
        droplet_env.action = droplet_env.human_step(event)
        if event.type == pygame.KEYDOWN:
            break
        
          
    

        
    #Update flowrates
    (droplet_env.Q1,droplet_env.Q2,droplet_env.Q3) = droplet_env.change_flow_rates(droplet_env.action,droplet_env.Q1,droplet_env.Q2,droplet_env.Q3)
        
    #calculate Droplet velocity
    (droplet_env.u,droplet_env.v) = droplet_env.calculate_drop_v(droplet_env.droplet_pos,droplet_env.Q1,droplet_env.Q2,droplet_env.Q3)
    
    #Update droplet position
    droplet_env.droplet_pos = droplet_env.new_position(droplet_env.u,droplet_env.v,droplet_env.droplet_pos,droplet_env.time_step)
    
    #Draw the droplet
    droplet_env.game_window.fill(BLACK)
    pygame.draw.circle(droplet_env.game_window, GREEN, droplet_env.droplet_pos*droplet_env.frame_size,20)
    
    #Check whether game is over or not
    droplet_env.game_over()
    
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
    img = array3d(droplet_env.game_window)
    
    
        
                
        

    

        
    