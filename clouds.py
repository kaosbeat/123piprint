# coding: utf-8
import svgwrite
import random
import math
cloudfontsize = 25
skylinefontsize = 25
patternfontsize = 25
basefontsize = 4

test = True
# test = False


debug = True
debug = False

def debugdefs():
	dwg.defs.add(dwg.style('.debug {opacity : 1.0; color:red; font-family: ss; visibility:hidden;}'))


printerBoxFrontPanel = True
printerBoxFrontPanel = False
printerBoxFrontPanelSize = (400,600)

printerBoxSidePanel = True
printerBoxSidePanel = False
printerBoxSidePanelSize = (410,400)

printerBoxTopPanel = True
printerBoxTopPanel = False
printerBoxTopPanelSize = (400,500)

pianoCoverInsidePanel = True
pianoCoverInsidePanel = False
pianoCoverInsidePanelSize = (1345,210)

pianoCoverOutsidePanel = True
pianoCoverOutsidePanel = False
pianoCoverOutsidePanelSize = (1345,325)

pianoBottomPanel = True
pianoBottomPanel = False
pianoBottomPanelSize = (1225,550)

pianoFrontPanel = True
pianoFrontPanel = False
pianoFrontPanelSize = (1305,270)

pianoTopPanel = True
pianoTopPanel = False
# pianoTopPanelSize = (1395,335) ### too small for long phrases
pianoTopPanelSize = (1375,320)

pianoBoxLeftPanel = True
pianoBoxLeftPanel = False
pianoBoxLeftPanelSize = (670,1350)

pianoBoxRightPanel = True
pianoBoxRightPanel = False
pianoBoxRightPanelSize = (670,1350)

pianoBoxLeftTrianglePanel = True
pianoBoxLeftTrianglePanel = False
pianoBoxLeftTrianglePanelSize = (750,400)

pianoBoxRightTrianglePanel = True
pianoBoxRightTrianglePanel = False
pianoBoxRightTrianglePanelSize = (750,400)

pianoBoxBackPanel = True
pianoBoxBackPanel = False
pianoBoxBackPanelSize = (1349,1667)

pianoBoxBackPanelSmall = True
pianoBoxBackPanelSmall = False
pianoBoxBackPanelSmallSize = (1349,1667-1220)

pianoBoxTopPanel = True
pianoBoxTopPanel = False
pianoBoxTopPanelSize = (1545,556)

pianoBoxFrontPanel = True
pianoBoxFrontPanel = False
pianoBoxFrontPanelSize = (1565,1080)

if test:
	dwg = svgwrite.Drawing('test.svg', size=("1440mm","1440mm"), profile='full')




# dwg.defs.add(dwg.style('svg {text-shadow: 3px 2px red;}'))
dwg.defs.add(dwg.style('svg {background-color: white;'))
# dwg.defs.add(dwg.style('svg {font-family: asciid;}'))
# dwg.defs.add(dwg.style('.cloud {font-family: Wonky Pins;}'))
# dwg.defs.add(dwg.style('.cloud {font-size: '+str(cloudfontsize)+'px;}'))
# dwg.defs.add(dwg.style('.cloud {opacity: 0.7;}'))
# dwg.defs.add(dwg.style('.skyline {font-family: Wonky Pins;}'))
# dwg.defs.add(dwg.style('.skyline {font-size: '+str(skylinefontsize)+'px;}'))
# dwg.defs.add(dwg.style('.skyline {white-space: pre; }'))

dwg.defs.add(dwg.style('.sqsq {font-family: Wonky Pins;}'))
dwg.defs.add(dwg.style('.fontww {font-family: ss;}'))
# dwg.defs.add(dwg.style('.fontww {font-family: Wonky Pins;}'))

dwg.defs.add(dwg.style('.font1 {font-size: '+str(basefontsize)+'px;}'))
dwg.defs.add(dwg.style('.font2 {font-size: '+str(basefontsize*2)+'px;}'))
dwg.defs.add(dwg.style('.font3 {font-size: '+str(basefontsize*3)+'px;}'))
dwg.defs.add(dwg.style('.font4 {font-size: '+str(basefontsize*4)+'px;}'))
dwg.defs.add(dwg.style('.font5 {font-size: '+str(basefontsize*5)+'px;}'))
dwg.defs.add(dwg.style('.font6 {font-size: '+str(basefontsize*6)+'px;}'))
dwg.defs.add(dwg.style('.font7 {font-size: '+str(basefontsize*7)+'px;}'))
dwg.defs.add(dwg.style('.sqsq {white-space: pre; }'))
dwg.defs.add(dwg.style('.debug {opacity : 1.0; color:red; font-family: ss; visibility:hidden;}'))
# dwg.defs.add(dwg.style('svg {font-family: ss;}'))

# dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
# dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))

# 

# cloud1.add(dwg.style('svg {font-family: Wonky Pins;}'))

xoffset = 150
yoffset = 150
xscale = cloudfontsize * 0.58
yscale = cloudfontsize * 0.8

# for i in xrange(-2,10):
	# for j in range(i,0):
		# cloud1.add(dwg.text('#', insert=((xscale*(i*-5)+(2*i)) + xoffset, yscale*j + yoffset ), fill='rgb('+str(j*10)+',20,23)'))

cloudheight = 23
returnpoint = 0.7




def putcloud(cloudid, text, posx, posy, cloudheight, returnpoint, xnoise, ynoise, xdensity):
	xsize = len(text)
	cloud = dwg.add(dwg.g(id="cloudid", class_="cloudgroup", transform="translate("+str(posx)+","+str(posy)+")"))  
	# style="font-family: Wonky Pins;", 
	cloud.add(dwg.text("debugtext", class_="debug"))
	# cloud.add(dwg.style('cloud {font-family: Wonky Pins;}'))
	for i in xrange(1,cloudheight):
		c = random.random() - 0.2
		basex = c * xscale * xsize
		y = i*yscale
		print(y)
		if i < int(returnpoint*cloudheight):
			for j in xrange(0,i*i+1):	
				x = basex + ((i - 2*i) +j) * xsize * xscale
				x = x + (0.5 - random.random()) * xnoise * xsize * xscale 
				x = x * xdensity
				# x = x * xsize
				# x = j * xsize * xscale
				y = y + yscale*ynoise*(random.random()-0.5)
				cloud.add(dwg.text(text, class_="cloud", insert=(x,y), fill='rgb('+str(j*1)+',20,23)'))
		else:
			for j in xrange(i*i+1,i*i+1 - int(cloudheight*returnpoint*i), -1):
				
				# x = basex + ((i - 2*i) + j - 2*i)
				# x = x * random.random() * xnoise
				# x = x * xsize
				x = basex + ((i - 2*i) +j) * xsize * xscale
				x = x + (0.5 - random.random()) * xnoise * xsize * xscale 
				x = x * xdensity
				y = y + yscale*ynoise*(random.random()-0.5)
				# x = basex + ((i - 2*i) + i - (returnpoint*cloudheight) + j ) * xscale
				cloud.add(dwg.text(text, class_="cloud", insert=(x,y), fill='rgb('+str(int(i)*1)+',20,23)'))




# putcloud("cloud1", "123", 200,100,15,0.7, 20, 0.2, 0.3)
# putcloud("cloud2", "piano", 400,800,10,0.8, 100,0.3, 0.1 )
# putcloud("cloud3", "de krook", 200,600,10,0.8, 70,0.3, 0.1 )
# putcloud("cloud4", "Gent", 600,1200,10,0.8, 70,0.3, 0.1 )







# for cloud in xrange(7):
# 	posx = random.random()*200
# 	posy =random.random()*1800
# 	cloudheight = int(random.random()*10)+5
# 	returnpoint = 0.2 + random.random()*0.4 
# 	xnoise =random.random()*0.4
# 	ynoise = random.random()*5
# 	xdensity = random.random()+0.3
# 	putcloud("cloud"+str(cloud), cloudwords[cloud], posx ,posy, cloudheight,returnpoint,xnoise,ynoise,xdensity )


# putcloud("cloud"+str(0), "Penty Harmonium"   ,100 ,100 ,15 ,0.7 ,0.4,0.2,0.9("cloud"+str(1), "Avril 14th"        ,300 ,400 ,5  ,0.6 ,0.2,0.1,0.4)
# putcloud("cloud"+str(2), "Nanou 2"           ,200 ,500 ,13 ,0.9 ,0.0,0.0,0.3)
# putcloud("cloud"+str(3), "aisatsana"         ,700 ,900 ,12 ,0.5 ,0.3,4.7,1.3)
# putcloud("cloud"+str(4), "Petiatil cx htdui" ,400 ,1200,19 ,0.6 ,0.1,0.1,1.1)
# putcloud("cloud"+str(5), "kesson daslef"     ,600 ,1600,11 ,0.7 ,0.1,0.2,0.12)
# putcloud("cloud"+str(6), "Jynweythek Ylow"   ,900 ,1800,9  ,0.7 ,0.9,0.2,0.9)


# putcloud("cloud"+str(0), "Penty Harmonium"   ,100 ,100 ,30 ,0.7 ,0.4,0.2,0.9)
# putcloud("cloud"+str(1), "Avril 14th"        ,300 ,400 ,10  ,0.6 ,0.2,0.1,0.4)
# putcloud("cloud"+str(2), "Nanou 2"           ,200 ,500 ,25 ,0.9 ,0.0,0.0,0.3)
# putcloud("cloud"+str(3), "aisatsana"         ,700 ,900 ,20 ,0.5 ,0.3,4.7,1.3)
# putcloud("cloud"+str(4), "Petiatil cx htdui" ,400 ,1200,40 ,0.6 ,0.1,0.1,1.1)
# putcloud("cloud"+str(5), "kesson daslef"     ,600 ,1600,29 ,0.7 ,0.1,0.2,0.12)
# putcloud("cloud"+str(6), "Jynweythek Ylow"   ,900 ,1800,20  ,0.7 ,0.9,0.2,0.9)

# putcloud("cloud"+str(5), "Penty Harmonium"  ,100 ,100 ,29 ,0.3 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "aisatsana"        ,1000,400 , 9 ,0.5 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "Avril 14th"       ,600 ,600 , 9 ,0.5 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "kesson daslef"    ,200 ,800, 19 ,0.6 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "Jynweythek Ylow"  ,-600 ,1200,12 ,0.4 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "Petiatil cx htdui",-600 ,1400,30 ,0.4 ,0.1,0.2,0.12)
# putcloud("cloud"+str(5), "Nanou 2"          ,80 ,1800 , 9 ,0.5 ,0.1,0.2,0.12)

# putcloud("cloud"+str(5), "Penty Harmonium"  ,100 ,100 ,12 ,0.3 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "aisatsana"        ,1000,400 , 9 ,0.5 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "aisatsana"        ,10,400 , 9 ,0.5 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "Avril 14th"       ,600 ,600 , 9 ,0.5 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "kesson daslef"    ,200 ,800, 9 ,0.6 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "Jynweythek Ylow"  ,-600 ,1200,12 ,0.4 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "Petiatil cx htdui",-600 ,1400,16 ,0.4 ,0.4,0.2,0.4)
# putcloud("cloud"+str(5), "Nanou 2"     		,80 ,1800 , 9 ,0.4 ,0.4,0.2,0.4)

afxtracks = ["Penty Harmonium","aisatsana" ,"Avril 14th" ,"kesson daslef","Jynweythek Ylow","Petiatil cx htdui","Nanou 2","QKThr", "Beskhu3epnm","father","Prep Gwarlek","Btoum-Roumada","Ruglen Holon","Strotha Tynhe","Kladfvgbung Micshk"]


def bottomcloud(cloudid, text, posx, posy, cloudheight, returnpoint, xnoise, ynoise, xdensity):
	xsize = len(text)
	cloud = dwg.add(dwg.g(id="cloudid", class_="cloudgroup", transform="translate("+str(posx)+","+str(posy)+")"))  
	# style="font-family: Wonky Pins;", 
	if debug:
		cloud.add(dwg.text("debugtext", class_="debug"))
	# cloud.add(dwg.style('cloud {font-family: Wonky Pins;}'))
	for i in xrange(1,cloudheight):
		c = random.random() - 0.5
		c = c*10
		# basex = 0
		y = i*yscale
		
		if i < cloudheight*returnpoint:
			for j in xrange(0,i):
				basex = (c - i)*xsize*xscale*xdensity/2
				# basex = 0
				x = basex + j*xsize*xscale*xdensity
				y = y + yscale*ynoise*(random.random()-0.5)
				cloud.add(dwg.text(text, class_="cloud", insert=(x,y), fill='rgb('+str(j*1)+',20,23)'))
		else:
			for j in xrange(0,cloudheight-i):
				j = j - (cloudheight-i) 
				basex = (c - j)*xsize*xscale*xdensity/2
				# print(basex)
				# basex = xscale*xsize*xdensity
				# basex = (c * xscale * xsize /2 - (j + i)*xsize*xscale)*xdensity/2 
				x = basex - (j+cloudheight-i)*xsize*xscale*xdensity
				# x = basex
				y = y + yscale*ynoise*(random.random()-0.5)
				cloud.add(dwg.text(text, class_="cloud", insert=(x,y), fill='rgb('+str(i*1)+',20,23)'))	


def multibottomcloud(size, text, x, y):
	for i in xrange(1,size):
		bottomcloud("cloud"+str(5), afxtracks[random.randint(0,len(afxtracks)-1)],x+(random.random()*50*i) ,y+(random.random()*50*size*i) ,int(random.random()*7 + 5) ,0.7 ,0.4,0.2,0.3)
	# bottomcloud("cloud"+str(5), text,1400 ,1200,15 ,0.5 ,0.4,0.2,0.3)
	# bottomcloud("cloud"+str(5), text,1000 ,1100,11 ,0.2 ,0.4,0.2,0.3)
# putcloud("cloud"+str(5), "Nanou 2"     		,80 ,1800 , 9 ,0.4 ,0.4,0.2,0.4)




def rotationdots (posx,posy):
	for j in xrange(1,360):
		dwg.defs.add(dwg.style('.dots {font-family: Wonky Pins;}'))
		dwg.defs.add(dwg.style('.dots {font-size: 15px;}'))
		dwg.defs.add(dwg.style('.dots {opacity: 1;}'))
		dotlayer = dwg.add(dwg.g(id="dot"+str(j), class_="dots", transform="translate("+str(posx)+","+str(posy)+") rotate("+str(j)+" 500 500)"))
		text = ".................................................."
		# text = "--------------------------------------------------"
		text="\ |//|   |//|   |//|   |//|   |//|   |//|   |//|   |//|   |//|   |//|   |//|   |//|  "
		# text = "mereljosseireensarahkaspermereljosseireensarahkaspermereljosseireensarahkasper"
		# text = "+*-/_"
		for i in xrange(1,25):
			text = afxtracks[random.randint(0,len(afxtracks)-1)]
			dotlayer.add(dwg.text(text, class_="dotrow", insert=(0,(i*200)), fill='black'))









def helix(height,width):
	pattern = [1,0,0,0,0,2,0,0,4,0,6,0,0,0,0,0,0,0,3,0,0,0,0,0,0,5,0,0]
	pattern2 = pattern
	nextpattern = []
	word = ["a","b","c","d"]
	for j in range(height):
		for index, item in enumerate(pattern):
			if item == 0:
				pattern2[index] = 0
			if item != 0:
				ind = index - 1
				if ind < 0:
					ind = len(pattern)-1
				# print ind
				pattern2[ind] = item
				if item == 2:
					print(j)
					pattern2[ind] = word[j]
				pattern2[index] = 0
			# if item == 2:
			# 	ind = index+1
			# 	if ind == len(pattern):
			# 		ind = 0
			# 	pattern2[ind] = 2
			# 	pattern2[index] = 0 
		print(pattern2)
		# print()

helix(100,10)


skyline = """
                                                                              <%<                                                                                                                     
                                                                               |                                                                                                                     
                                                                               %                                                                                                                     
                                               [                               %                                                                                                                     
                                               [                              %%%                                                                                                                    
                                               ]                              %%%                                                                                                                    
                                           %  % #   %                        %%%%%                                                                        %                                           
                                           % %%%%%% %                     %  %%%%%%  %                                                                   %%                                         
                                          %%% %%%% %%%                    % %%%%%%%% %                                                             %    %%%%%   %                                    
                                          %%% %%%% %%%                    %%%%% %%%%%%                                                            ,%% %%%%%%%%% %%                                   
                                          %%%%%%%%%%%%                    %%%%    %%%%                                                            (%%%%%%%%%%%%%%%                                   
                                          % %% %%% % %                    %%%%    %%%%                                                            (%%%%%%%%%%%%%%%                                   
                                          % %% %%% % %                    %%%%    %%%%                                                            (%%%%%%%%%%%%%%%                                   
                                          % %% %%% % %                    %%%%%%%%%%%%                                                            (%%%%%%%%%%%%%%%                                   
                                          %%%%%%%%%%%%                    %%  %%%%  %%                                                            (%%%%%%%%%%%%%%%                                   
                                          % %% %%% % %                    %%  %%%%  %%                                                            (%%%%%%%%%%%%%%%                                   
                                          % %% %%% % %                    %%  %%%%  %%                                                            (%%%%%%%%%%%%%%%                                   
                                         %% %% %%% % %%                   %%%%%%%%%%%%                                                        %   (%%%%%%%%%%%%%%%    %                              
                  #.                     %%%%%%%%%%%%%%                   %%  %%%%  %%                                                       (%%  %%%%%%%%%%%%%%%%%  %%               %    %         
                %%%%%%%%%%%/             %%%%%%%%%%%%%%                   %%  %%%%  %%                                              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(%%(             .%(   %.        
                %%%%%%%%%%%%%            %%%%%%%%%%%%%%                   %%  %%%%  %%                                             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
.%%%%%%. (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        .%%%%%%%%%%%%%%%%                           %%%%%%%%/        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     %%%%%%%%%%%%%%%%%%%%     %%%%%%%%%%,,,.      ,%%%%%%%%%%%/%**  .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*       
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

t="""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

# skyline = """hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"""

hollowbox = """
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhh                               hhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
"""


onderdemaan = ["Onder de maan schuift de lange rivier","Over de lange rivier schuift moede de maan","Onder de maan op de lange rivier schuift de kano naar zee","Langs het hoogriet","langs de laagwei","schuift de kano naar zee","schuift met de schuivende maan de kano naar zee","Zo zijn ze gezellen naar zee de kano de maan en de man","Waarom schuiven de maan en de man getweeën gedwee naar de zee"]





strategies = [ "(Organic) machinery", "A line has two sides", "A very small object: Its center", "Abandon desire", "Abandon normal instructions", "Abandon normal instruments", "Accept advice", "Accretion", "Adding on", "Allow an easement (an easement is the abandonment of a stricture)", "Always first steps", "Always give yourself credit for having more than personality (given by Arto Lindsay)", "Always the first steps", "Are there sections?  Consider transitions", "Ask people to work against their better judgement", "Ask your body", "Assemble some of the elements in a group and treat the group", "Balance the consistency principle with the inconsistency principle", "Be dirty", "Be extravagant", "Be less critical", "Breathe more deeply", "Bridges   -build   -burn", "Bridges -build -burn", "Cascades", "Change ambiguities to specifics", "Change instrument roles", "Change nothing and continue consistently", "Change nothing and continue with immaculate consistency", "Change specifics to ambiguities", "Children   -speaking     -singing", "Cluster analysis", "Consider different fading systems", "Consider transitions", "Consult other sources   -promising   -unpromising", "Convert a melodic element into a rhythmic element", "Courage!", "Cut a vital conenction", "Cut a vital connection", "Decorate, decorate", "Define an area as `safe' and use it as an anchor", "Destroy  -nothing   -the most important thing", "Destroy nothing; Destroy the most important thing", "Discard an axiom", "Disciplined self-indulgence", "Disconnect from desire", "Discover the recipes you are using and abandon them", "Discover your formulas and abandon them", "Display your talent", "Distort time", "Distorting time", "Do nothing for as long as possible", "Do something boring", "Do something sudden, destructive and unpredictable", "Do the last thing first", "Do the washing up", "Do the words need changing?", "Do we need holes?", "Don't avoid what is easy", "Don't be frightened of cliches", "Don't break the silence", "Don't stress on thing more than another [sic]", "Don't stress one thing more than another", "Dont be afraid of things because they're easy to do", "Dont be frightened to display your talents", "Emphasize differences", "Emphasize repetitions", "Emphasize the flaws", "Faced with a choice, do both (from Dieter Rot)", "Faced with a choice, do both (given by Dieter Rot)", "Feed the recording back out of the medium", "Fill every beat with something", "Find a safe part and use it as an anchor", "Get your neck massaged", "Ghost echoes", "Give the game away", "Give the name away", "Give way to your worst impulse", "Go outside.  Shut the door.", "Go outside. Shut the door.", "Go slowly all the way round the outside", "Go to an extreme, come part way back", "Honor thy error as a hidden intention", "Honor thy mistake as a hidden intention", "How would someone else do it?", "How would you have done it?", "Humanize something free of error", "Idiot glee (?)", "Imagine the piece as a set of disconnected events", "In total darkness, or in a very large room, very quietly", "Infinitesimal gradations", "Intentions   -nobility of  -humility of   -credibility of", "Into the impossible", "Is it finished?", "Is something missing?", "Is the information correct?", "Is the style right?", "Is there something missing", "It is quite possible (after all)", "It is simply a matter or work", "Just carry on", "Left channel, right channel, center channel", "Listen to the quiet voice", "Look at the order in which you do things", "Look closely at the most embarrassing details & amplify them", "Lost in useless territory", "Lowest common denominator", "Magnify the most difficult details", "Make a blank valuable by putting it in an exquisite frame", "Make a sudden, destructive unpredictable action; incorporate", "Make an exhaustive list of everything you might do & do the last thing on the list", "Make it more sensual", "Make what's perfect more human", "Mechanicalize something idiosyncratic", "Move towards the unimportant", "Mute and continue", "Not building a wall but making a brick", "Not building a wall; making a brick", "Once the search has begun, something will be found", "Only a part, not the whole", "Only one element of each kind", "Openly resist change", "Overtly resist change", "Pae White's non-blank graphic metacard", "Put in earplugs", "Question the heroic", "Question the heroic approach", "Reevaluation (a warm feeling)", "Remember quiet evenings", "Remember those quiet evenings", "Remove a restriction", "Remove ambiguities and convert to specifics", "Remove specifics and convert to ambiguities", "Repetition is a form of change", "Retrace your steps", "Reverse", "Short circuit (example; a man eating peas with the idea that they will improve  his virility shovels them straight into his lap)", "Simple Subtraction", "Simple subtraction", "Simply a matter of work", "Slow preparation, fast execution", "Spectrum analysis", "State the problem as clearly as possible", "State the problem in words as clearly as possible", "Take a break", "Take away the elements in order of apparent non-importance", "Take away the important parts", "Tape your mouth (given by Ritva Saarikko)", "The inconsistency principle", "The most easily forgotten thing is the most important", "The most important thing is the thing most easily forgotten", "The tape is now the music", "Think - inside the work -outside the work", "Think of the radio", "Tidy up", "Towards the insignificant", "Trust in the you of now", "Try faking it (from Stewart Brand)", "Turn it upside down", "Twist the spine", "Use 'unqualified' people", "Use `unqualified' people", "Use an old idea", "Use an unacceptable color", "Use cliches", "Use fewer notes", "Use filters", "Use something nearby as a model", "Use your own ideas", "Voice your suspicions", "Water", "What are the sections sections of?    Imagine a caterpillar moving", "What are you really thinking about just now?", "What context would look right?", "What is the reality of the situation?", "What is the simplest solution?", "What mistakes did you make last time?", "What to increase? What to reduce? What to maintain?", "What were you really thinking about just now?", "What would your closest friend do?", "What wouldn't you do?", "When is it for?", "Where is the edge?", "Which parts can be grouped?", "Work at a different speed", "Would anyone want it?", "You are an engineer", "You can only make one dot at a time", "You don't have to be ashamed of using your own ideas"]

def skylinedefs():
	dwg.defs.add(dwg.style('.skyline {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.skyline {font-size: '+str(skylinefontsize)+'px;}'))
	dwg.defs.add(dwg.style('.skyline {white-space: pre; }'))

def doskyline(skyline, posx, posy, charscale, rot, scale, rand, vertskyscale):
	skylinedefs()
	skylinedata = skyline.splitlines()
	# print(skylinedata)

	#create svgelement
	skyline = dwg.add(dwg.g(id="skyline", class_="skyline", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+"), scale("+str(scale)+")"))  
	#start adding chars
	charcount = 0
	strategycount = 0
	charscalecount = 0
	strategy = strategies[strategycount]
	if rand:
		strategy = strategies[random.randint(0,len(strategies)-1)]

	for i,l in enumerate(skylinedata): 
		for cscl in xrange(charscale):
			newline = ""
			for c in l:
				charscalecount = 0
				if charscalecount < charscale:
					if c == " ":
						for csc in xrange(charscale):
							newline = newline + " "
					else:
						for csc in xrange(charscale):
							newline = newline + strategy[charcount]
							charcount = charcount+1
							if charcount == len(strategy):
								charcount =0
								strategycount = strategycount + 1
								if strategycount == len(strategies):
									strategycount=0
								strategy = strategies[strategycount]
								if rand:
									strategy = strategies[random.randint(0,strategycount)]
							# print(newline)
				charscalecount = charscalecount + 1
			skyline.add(dwg.text(newline, class_="skyline", insert=(0,((i*charscale+cscl)*(vertskyscale*skylinefontsize))), fill='black'))




####emoticons

			# "<(-'.'-)>", 
			
			# "(>';.;')>"]

def river(length,posx,posy,rot,scale,texts):
	skylinedefs()
	sinesweep = 0
	river = dwg.add(dwg.g(id="river", class_="skyline", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+"), scale("+str(scale)+")"))
	for x in xrange(length):
		text = texts[random.randint(0,len(texts)-1)]
		textlength = len(text)
		river.add(dwg.text(text, class_="skyline", insert=(math.sin(3.14/50*x)*250,25*x), fill='black'))

def river2(length,posx,posy,rot,xtrarot,scale,texts):
	river2fontsize = 12
	dwg.defs.add(dwg.style('.river2 {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.river2 {font-family: Courier New;}'))
	dwg.defs.add(dwg.style('.river2 {font-size: '+str(river2fontsize)+'px;}'))
	dwg.defs.add(dwg.style('.river2 {white-space: pre; }'))
	sinesweep = 0
	river2 = dwg.add(dwg.g(id="river", class_="river2", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+"), scale("+str(scale)+")"))
	for x in xrange(length):
		text = texts[random.randint(0,len(texts)-1)]
		textlength = len(text)
		river2.add(dwg.text(text, class_="river2", insert=(math.sin(3.14/50*x)*250,18*x), fill='black', transform="rotate("+str(x*xtrarot)+")"))


def emocrowd(posx, posy, sleepy):
	emofontsize = 20

	emolist1 = [ "ò_ó", "ó_ò", "õ_o", "ù_u", "o_Ô", "-O-", "-3-", "-w-", "'_'", ";_;", "ʘ‿ʘ","(⊙_☉)"]
	emolist2 = ["<(^.^)>", "<('.')^", "<(^_^<)", "<(o_o<)","( ˇ෴ˇ )", "(　＾∇＾)", "(~‾▿‾)~", "( ￣▽￣)/"]
	emolist3 = ["[(-_-)]"]			 
			
	dwg.defs.add(dwg.style('.emogroup {font-family: Courier;}'))
	dwg.defs.add(dwg.style('.emogroup {font-size: '+str(emofontsize)+'px;}'))
	dwg.defs.add(dwg.style('.emogroup {white-space: pre; }'))
	emos = dwg.add(dwg.g(id="emoid", class_="emogroup", transform="translate("+str(posx)+","+str(posy)+")"))  
	xcursor = 0
	for j in xrange(15):
		xcursor = 0
		for i in xrange(90):
			emolist = random.randint(1,2)
			# print(emolist)
			if emolist == 1:
				text = emolist1[random.randint(0,len(emolist1)-1)]
				xspace = 4
			if emolist == 2:
				text = emolist2[random.randint(0,len(emolist2)-1)]
				xspace = 8		
			# print(len(text))
			x = xcursor + (random.random()-0.5)*30
			y = j * 60 + (random.random()-0.5)*30
			# print (x,y)
			if sleepy:
				text = "(-_-)"
				x = xcursor
				y = j* 100
				xspace =4
			emos.add(dwg.text(text, class_="emogroup", insert=(x,y),fill = "black" )) ##fill='rgb('+str(j*20)+',0,23)' 
			xcursor = xcursor + 0.8*xspace*emofontsize




###########################
##### CLOUDS ##########
###########################





# doskyline(skyline, 1250+625, 0,2,45,0.707)
# doskyline(skyline, 1250+625+625+313, 625+313,2,90,0.707*0.707)


def clouddefs():
	dwg.defs.add(dwg.style('.cloud {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.cloud {font-size: '+str(cloudfontsize)+'px;}'))
	dwg.defs.add(dwg.style('.cloud {opacity: 0.7;}'))


### topwallpanel 1440x780
cloudwords = ["Penty Harmonium", "Avril 14th", "Nanou 2", "aisatsana", "Petiatil cx htdui", "kesson daslef", "Jynweythek Ylow" ]
# cloudwords = strategies
# dwg.add(dwg.rect(("0mm","0mm"),("1440mm","780mm"), fill="red"))

# for cl in xrange(12):
# 	multibottomcloud(random.randint(3,8), cloudwords[random.randint(0,6)], (cl + (random.random() - 0.5)) * 500, random.randint(0,1500))

###########################
#### pianoBox ##########
###########################

def pianoBoxTop():
	clouddefs()
	cloudwords = strategies
	# dwg.add(dwg.rect(("0mm","0mm"),("1440mm","780mm"), fill="red"))
	for cl in xrange(12):
		multibottomcloud(random.randint(3,8), cloudwords[random.randint(0,6)], (cl + (random.random() - 0.5)) * 500, random.randint(0,1500))

def pianoBoxBack():
	cloudwords = strategies
	# dwg.add(dwg.rect(("0mm","0mm"),("1440mm","780mm"), fill="red"))
	for cl in xrange(12):
		multibottomcloud(random.randint(3,8), cloudwords[random.randint(0,6)], (cl + (random.random() - 0.5)) * 500, random.randint(0,1500))

def pianoBoxFront():
	clouddefs()
	cloudwords = strategies
	# dwg.add(dwg.rect(("0mm","0mm"),("1440mm","780mm"), fill="red"))
	for cl in xrange(18):
		multibottomcloud(random.randint(3,8), cloudwords[random.randint(0,6)], (cl + (random.random() - 0.5)) * 500, random.randint(0,1500))





###########################
##### SIDEPANELS ##########
###########################


geopattern1 = """
	 __________
	/         /
   / _____   /
  / /       /
 / /       /
/_/______/
 
""" 

def flatsquare(size, debugstr,  debug):
	sq = ""
	for x in xrange(size):
		print(x)
		for y in xrange (size-x):
			sq = sq + " "
		if x == 0:
			for y in xrange(size*2-1):
				sq = sq + "_"
		elif x == size-1:
			sq = sq + "/"
			for y in xrange(size*2-2):
				sq = sq + "_"
			sq=sq+"/"
		else:
			sq = sq + "/"
			for y in xrange(size*2-2):
				sq = sq + " "
			sq=sq+"/"
		sq=sq+"\n"
	if debug:
		sq = sq + debugstr
	return sq

hsq = """ 
12345678901234567890
12345678901234567890
12                90
12                90
12                90
12                90
"""


def hollowsquare(size):
	hsq = ""
	for x in xrange(size):
		print(x)

def patternsetdefs():
	dwg.defs.add(dwg.style('.pattern {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.pattern {font-size: '+str(patternfontsize)+'px;}'))
	dwg.defs.add(dwg.style('.pattern {white-space: pre; }'))



def geopattern(pattern,posx,posy):
	charscale = 1
	patterndata = pattern.splitlines()
	geopattern = dwg.add(dwg.g(id="geopattern", class_="geopattern", transform="translate("+str(posx)+","+str(posy)+")"))
	for i,l in enumerate(patterndata):
		newline = ""
		for c in l:
			newline = newline + c	
		geopattern.add(dwg.text(newline, class_="pattern", insert=(0,((i*charscale)*(0.8 *patternfontsize))), fill='black'))
	return geopattern




def multigeopattern(totalp,sizex,sizey, noise):
	for p in xrange(totalp):
		xpos = random.randint(0,sizex)
		xoff = random.randint(0,30)-15
		ypos = random.randint(0,sizey)
		yoff = random.randint(0,50)-25
		for t in xrange(random.randint(5,25)):
			if noise:
				xoff = random.randint(0,15)-8
				yoff = random.randint(0,25)-12
			geopattern(flatsquare(t,"",False), xpos+t*yoff, ypos+t*yoff)

# multigeopattern(20,1000,1500,False)


def patternstudy(size, debug, noise):
	yoffset = 100
	xoffset = 40
	rows = 10
	cols = 6
	for r in xrange(rows):
		ypos = r*500 + yoffset
		for c in xrange(cols):
			xpos = c*400 + xoffset
			yoff = c*2 - cols/2
			xoff = r*2 - rows/2
			if noise:
				xoff = xoff+random.randint(0,15)-8
				yoff = yoff+random.randint(0,25)-12
			for t in xrange(size):
				pat = geopattern(flatsquare(t, "x-offset = " + str(xoff) , debug), xpos+t*xoff, ypos+t*yoff)
		pat.add(dwg.text("x-offset = " + str(xoff), class_="pattern", insert=(0,0), fill='black'))

# patternstudy(20)

# def musicdimension():
# 	dosqsq(5,3,200,200,0,"music")
# 	dosqsq(5,2,200,200,45,"piano")


def dosqsq(index, size,posx, posy, rot, text):
	sqsq = dwg.add(dwg.g(id="sqsq"+str(index) ,  class_="sqsq", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+")"))
	sqline = ""
	for side in xrange(4):
		rot = side*90
		tx = 0
		ty = 0
		if (side == 1):
			tx = 90
			ty = -423 
		if (side == 2):
			tx = -330
			ty = -513
		if (side == 3):
			tx = -425
			ty = -93 
		for s in xrange(size):
			for c in xrange(size*10):
				sqline = sqline + text[random.randint(0,len(text)-1)]
			sqline = sqline + "\n"
			sqsqside = sqsq.add(dwg.g(transform="rotate("+str(90*side)+"),translate("+str(tx)+","+str(ty)+")"))
			sqsqside.add(dwg.text(sqline, class_="font"+str(index) , insert=(0, 100+basefontsize*size*s), fill='black'))
			sqline = ""

# musicdimensixon()




########################
### printerbox FRONT ###
########################


printerboxfontsize = 20
def printerBoxFront():
	# dwg = svgwrite.Drawing('printerBoxFront.svgwriteg', size=("500mm","400mm"), profile='full')
	dwg.defs.add(dwg.style('.feeder {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.feeder {font-size: '+str(printerboxfontsize)+'px;}'))
	dwg.defs.add(dwg.style('.feeder {white-space: pre; }'))
	feedmeweirdmusic(2250,50,90, True)
	# feedmeweirdmusic(2000,0,90, True)

def feederdefs():
	dwg.defs.add(dwg.style('.feeder {font-family: Wonky Pins;}'))
	# dwg.defs.add(dwg.style('.feeder {font-family: Courier;}'))
	dwg.defs.add(dwg.style('.feeder {font-size: '+str(printerboxfontsize)+'px;}'))
	dwg.defs.add(dwg.style('.feeder {opacity: 1;}'))



def feedmeweirdmusic(posx,posy,rot,invert):
	xcounter = 0
	cols = ["feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles","and","it","will","flow","and","grow","like","a","waterfall","grows","from","a","glacier","that","melts","like","it's","2019"]
	colsstate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	# colsstate = [1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	feeder = dwg.add(dwg.g(id="feeder" ,  class_="feeder", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+")"))
	for row in xrange(1,350):
		for col in xrange(len(cols)):
			# print(row%(col+1))
			if (row%(col+1) == 0):
				if (colsstate[col] == 1):
					colsstate[col] = 0
				elif (colsstate[col] == 0):
					colsstate[col] = 1
			# print(colsstate)
			if invert:
				if (colsstate[col] == 0):	
					feeder.add(dwg.text(cols[col], class_="fontww" , insert=(xcounter*printerboxfontsize/1.75, printerboxfontsize*row/2), fill='black'))
			else:
				if (colsstate[col] == 1):
					feeder.add(dwg.text(cols[col], class_="fontww" , insert=(xcounter*printerboxfontsize/1.75, printerboxfontsize*row/2), fill='black'))
			xcounter = xcounter + len(cols[col])
		xcounter = 0	




#####################
#####printer side####
#####################


printerboxsidefontsize = 24
def printerBoxSide():
	# dwg = svgwrite.Drawing('printerBoxSide.svg', size=("500mm","400mm"), profile='full')
	dwg.defs.add(dwg.style('.block {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.block {font-size: '+str(printerboxsidefontsize)+'px;}'))
	dwg.defs.add(dwg.style('.block {white-space: pre; }'))
	printblock(circuit,40,150,1.3,printerboxsidefontsize)

circuit = """
                                                            VCC        _
           |                                        +        / \         _
           V    musical transglorifier              --------(- +)-------/ \ |
           -           |                                     \_/       (Mic)| audience emotionizer
          /|          \-/                                            o--\_/ |
10Kv o--.  |          ===                                            |
        |  |          +|              analog transmogrifier         _-_
        | / \         _|_/                  |                      |___|
        |(_/_)        V_A                  / \                       -
        | \_/          |                  ( ~ )                      |
        |  |           |                   \_/                       |
        |  |           '-------.            |                        |
        -  -                   |            |                        |
       ------                  |            |                        |
        |  |                   |            v                        |
        |  |                   |        /|  ---  ___                 |
        uuuu ___   ||   .-.    |       /+|--+ +--UUU-------.         |
        ----|___|--||--( X )---o------<  |                 |  ___    |     __
        nnnn       ||   '-'    |       \-|-->|-----.       '-|___|---o-----  \ 
        |  |                   |        \|         |                      |   )o.
        |  |                   |                   |                   '--|__/  |
       ------                  |                   |                   |        |
        -  -                   |                   |      __           |        |     __ /|
        |  |                   |         _         '-----\  \      /|  |        '----|  | |
        |  |                  ---  ||   | |  +[/          |  |o--O< |--.        .----|__|<->
        | / \               .-v \--||--|| ||--[|---------/__/      \|  |        |        \|
        |(_\_)              |      ||   |_|   [\                       |   __   |
        | \_/               |                                          '--|  \  |               
        |  |                |                                             |   )-'              
        |  |             _  |                                          ---|__/                
        |  |       \]   | | |                             __           |      .----^--------^----.  
        |  o-------|]--|| ||'--------o-------o-----------\  \      /|  |      |   Printout  Bot  |  
GND o---'  C|      /]+  |_|          |       |            |  |o--O< |--o------o_-_-_-_-_-_-_-_-_-|
           C|                        |       |        ---/__/      \|     .---o o             o  |
           C|                  _     |      ---       |                   |   '---o             o'
           |                 -o-\_/o-o      ---       |                   |         o-------------o
           |                 |       |       |        |                   |         o             o
           C|                |       |       |        |                   |         o   .-.  .    o
           C|                |       |       |        |                   |         o   | 0  |    o
           C|                |       |       |        |                   |         o   0    0    o
           |            ___  |  ___  |  ___  |  ___   |                   |         o             o
           o-----------|___|-o-|___|-o-|___|-o-|___|--o-------------------'         o             o
           |                                          |                             o-------------o
           |                                         ===                             o             o
      piano inductor                                 GND                              o             o
                                                                                       o             o
                                                                                        o  © 2019     o
                                                                                         o []<> kaotec o
                                                                                          o-------------o
"""


instructions = """
 ____________________________________            
|\                                    \          
| \                                    \         
|  \____________________________________\        
|  |                      5.            |
|  |   2.       7.             7.   6.  |        
|  |  ________________________________  |        
|  | |________________________________| |        
|   \ \        1.            4.        \ \ 
|  \ ||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\| |
|  |\  ,--------------------------------  |
|  ||| |                               || |  0.  
 \ ||| |                               || |---= 
  \'|| |-------------------------------|| |
    \|_|                               \|_|
"""

tweetperson = """

      ///////\\
      |      |          3.
     O  o  -  O         ___
      |  ``  |         |#12| 
       \  - /          |3pi|
     ___|  |___        |ano|
    /   \__/   \      / ---
   /            \    / /
  /  /|   || |\  \  / /
 /  / |      | \  \/ /
{  {  |      |  \   /
 \  \ |      |   \_/
  \  \|______|
    \_|__K___|
      |      |
      |  |   |
      |  |   |
      |  |   |
      |  |  |
      (  (  |
      |  |  |
      |  |  |
   ___|__|  |
 [____[______)
"""
rtfm = """
RTFM
0. plug piano into 230VAC and wait for welcome message
1. play piano and enjoy or be bored by improv text
      either way, it cannot be silenced
2. if you played nice you might get a print
3. look on twitter for #123piano, this piano tweets!
4. go back to step 1
5. in case of problems read technical manual
6. always read .nfo files
7. jibberjabber examples, these are the words of the bot
"""
nfo = """                                                                                                                
                                                                                                                                                               
                                                                ***..                     ..***                                                                
                                                    ****,     ,  *,   ** **...   .. .*, *.  ,* .**     .****                                                   
                                             ,. .*****         .***,,,***.     *.    ,**,...,,**.         *****..,.                                            
                ***             ,**,,.   ****,.    ,*****, ,**            * ,*   ,* ,*           ,**  ******,   .*****   ...**.             ***                
                .***             .**********           ,  ***   .*.  ***,***  * ,*  ******,  **   ***. ,           **********.             ****                
           *****  *                 ************.  *  ,   ********.    ,,, ,*.    **. .,.    ******.**  *  *. ,************                 ,,  ****.          
             ,**,  ******** .****,  .*         *.  **              *,**  *.,        *.* **.**             ,*  .*.        *.   ****,  *******   ***             
         *******  .*   ,*,  **            **, .* **                 ***,  *         *.  ,*,                 ,* ., .**.           *** .**   ,*  .******         
        **     *****.        .**********.  **   *,  ..               **.,*           ,****                .   *,  ,*  .**********,         *****.    **.       
          ,        .*****,....,***,.       ,    **  ***                                                 ***. **.            ,**,..   .,*****.        .         
                                            *.                                                                    *.                                           
                                          **     **                                                         ,*,    **                                          
                                          .********                                                         ,********                                          

                                                                                        .                                          
                                   oe      .--~*teu.      .x~~"*Weu.                     @88>                                        
                                 .@88     dF     988Nx   d8Nu.  9888c     .d``           %8P                  u.    u.          u.   
                             ==*88888    d888b   `8888>  88888  98888     @8Ne.   .u      .          u      x@88k u@88c.  ...ue888b  
                                88888    ?8888>  98888F  "***"  9888%     \%8888:u@88N   .@88u     us888u.  ^"8888""8888"  888R Y888r 
                                88888     "**"  x88888~       ..@8*"       `888I  888. ''888E` .@88 "8888"   8888  888R   888R I888> 
                                88888          d8888*`     ````"8Weu        888I  888I   888E  9888  9888    8888  888R   888R I888> 
                                88888        z8**"`   :   ..    ?8888L      888I  888I   888E  9888  9888    8888  888R   888R I888> 
                                88888      :?.....  ..F :@88N   '8888N    uW888L  888'   888E  9888  9888    8888  888R  u8888cJ888  
                                88888     <""888888888~ *8888~  '8888F   '*88888Nu88P    888&  9888  9888   "*88*" 8888"  "*888*P"   
                                88888     8:  "888888*  '*8"`   9888%    ~ '88888F`      R888" "888*""888"    ""   'Y"      'Y"      
                             '**888888**  ""    "**"`     `~===*%"`         888 ^         ""    ^Y"   ^Y'                            
                                                                            *8E                                                      
                                                                            '8>                                                      
                                                                            "                                                       
                                            ,.                                                                  *****                                          
                                            **  ,*,                                                              **   **                                         
                .*       .,,,,..           *                                                                       *                                           
                ,******,*       .,,,.*,   *   ** ,*                                                        .** ,*   .    ,**.    .****      ,                  
                        *,  ** **       .*..* *.                                                               * ,*..**,    .**      ****. .**                 
                            .,,    ..  ,*     *. .*                                            ..              ,*  ,,       .  ** **  **   .,.                   
                                        .********.,, ,      ***. .***,                       ** .** **,*      ,  *     .,**,       ,**,                           
                                    ,****.***       .**,     .*. *.  *              **,,***.*     .*,     .**,      *******                                      
                                            .  ,**,  .  ,*.        ,***,   **       ,     ,***       ,** .****.  .***. ,***.                                    
                                                ***,   ..         ,                       , . ..           ****,,.                                             
                                                            *,                                   ,*        ..                                                   

                                                        >123 Piano Robo Voice Poet by Kasper Jordaens<
                                        ÕÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÑÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¸
                                        ³ SOFTWARE .. : pianotalk3000        ³ COMPANY ... : kaotec []<>             ³
                                        ³ SUPPLIER .. : 123piano             ³ CRACKER ... : not needed              ³
                                        ³ RATING .... : 5 stars :D           ³ PACKAGER .. : blackbirds & old piano  ³
                                        ³ ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ ³
                                        ³ GRAFIX .... : textfilesonly        ³ SOUND ..... : Awesome                 ³
                                        ÔÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¾

                                        ÕÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¸
                                        Notes: Can computer brains contribute to creative processes? 
                                        Is that robot a partner or is it rather part of the results. 
                                        This type of questions is what Kasper Jordaens tries to answer by setting 
                                        up collaborations between computers and willing guinea pigs. 123-piano 
                                        offers you a chance to try this first hand by playing the piano 
                                        (you can use a second hand as well ;-) that talks back while you play music, 
                                        giving sound advice on matters of life and making music. 

                                            GREETZ Go to: Sioen, Anders, Zbyszek and other people at Quatre Mains for
                                                thinking along in building the case and köhn for making music with it
                                                and everybody else for being here. Some art was adapted, but never
                                                copied from the great internetpeople! Thanks ascii scene
                                        ÔÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¾

                                        ÆÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍµ
                                        ³                           :: kaotec []<> 2019 ::                         ³
                                        ³ There will be bugs, easter eggs and risk for electroshocks. Make music   ³
                                        ³ at your own risk. The voice can not be turned off nor can someone be     ³
                                        ³ held responsible for whatever it says. Listen at your own risk.          ³
                                        ÔÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¾

                                        -*- Don't forget to wash your hands after touching Artificial Intelligence -*-

                                        ÕÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¸
                                        ³ contact me on twitter or instagram @kaosbeat                               ³
                                        ³                                                                            ³
                                        ÔÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¾
                                                                -=- We LoVe Robots Too! -=-

                                                                                  .*///,                                                                       
                                                                            ///\%\%\%\%\%\%\%\%\%\%\%//                                                                   
                                                                           //*         //#\%\%#/                                                                 
                                                                      //                  /\%\%\%/                                                                
                                                    /#/             /#/*         //\%\%\%\%/*  /%\%/                                                                
                                                 ./%/*            ////         ///////(%/  */%/                                                                
                                                /##/             */#/        ///,    /%(/  ./%/                                                                
                                               /#(/              ,/%/       ///     ///,   /((/                                                                
                                              ./%/               ./%#/     /%(/   /#/*     /%/                /.                                               
                                              /%(*                 /(#///,./#//// /       /#/                //,                                               
                                              /\%\%/                  .//#%\%\%\%\%//          ///               ./#/                                                
                                              ./%/                         /\%\%/          /                /##/                                                 
                                               /\%\%/                         /#%//    /                  /#%/*                                                  
                                                /\%\%//                        ./\%\%(/#//               //\%\%//                                                    
                                                 */\%\%//                     *//(#/\%\%\%///,       ///(\%\%//                                                       
                                                   //\%\%\%///.        ./////\%\%(//    ///\%\%\%\%\%\%\%\%\%\%\%(//,                                                          
                                                      ///\%\%\%\%\%\%\%\%\%\%\%\%\%#///,                                                                                    
                                                            ,////*.                                                                                            
                                                                                                                                                                            
"""
frameBL = """

                 #@@@@@(                                                                           
              .     %@@@@@@                                                                        
        &@        /@@  ,@@@@@                                                                      
      @              ,@%  @@@@#                                                                    
     @                 .@, %@@@#                                                                   
    @            *@@*    @& *@@@.                                                                  
    &   /@@@@@&     @@.   @& &@@@                                                                  
    &  %@@@@@@@&      @%  .@  @@@(                                                                 
     & %@@@@@@@&       *@  @@ (@@@                                                                 
       &.@@@@@*          % *@  @@@  @                                                              
                         * ,@  @@@ /@                                                              
         @@@@@(           .*@  @@@ @@                                                              
               &@         ,&@  @@& @@                                                              
                 .&   %@@@ @# (@@  @/                                                              
                   % *@@@@@@  @@& #@                                                               
                   . @@@@@@@ #@@  @                                                                
                     @@@@@@  @@* &/                                                                
      (&@@@      @@@#@@@@@  @@& /@                                                                 
           *@   @@@@@@@@@* &@&  %                                                                  
             @ #@@@@@@@@& @@&  #                                                                   
              ,&@@@@@@@( @@# /.   (@@@@@@@@@                                                       
               &@@@@@@% @@. & (@@(                                                                 
           *@@@/@@@@@( @@   &  *%&,                                                              
          @@@@@@@@@@( @@  ,.  /%&%*    @&                                                          
         @@@@@@@@@@% @&  *@@@@@@@@@@@@@  @@                                                        
        *@@@@@@@@@( @, @@@@@*      (@@@@& (@                                                       
        %@@@@@@@@& @.%@@@       .&@&. @@@@ @@                                                      
        &@@@@@@@@ @ @@@       @@@@@@@@.&@@//@                                                      
        (@@@@@@@ @ @@/       &,@@@@@@@&.@@#%@                                                      
         @@@@@@ //@@.        @#%@@@@@@ @@@ @@                                                      
         @@@@@& @%@.          @@     ,@@@                                                          
         %@@@@ & @,     (@@@@*  @@@@@@@                                                            
          @@@@ @(@   @,       @@(                                                                  
          @@@& *@  @            @@                                                                 
           @@#  @ .              @@                                                                
           ,@%  &(  @@@@@@@*     *%                                                                
       @@@  @@  (  @@/     &@#                                                                     
       @@@   @ */            &@ .                                       (@@@@@@@@@@@#              
       @@@@   @               &  %      #@@@/        ,             /@*   ,#@@@@@(    &@@@          
       #@@@(  (/              (  @   @       @@*    /@%   @@    /*  #@@@@@(.   ,%@@@@   @@@        
        %@@@.  /&             @  \%  \%         @@(   #@(  #@%  /  @@@%               (@@,  @@&      
         ,@@@@   &(         /   @  %           .    @@   @%* ,@@@                     .@@  #@@     
           @@@@/    %@\%\#%@(   #@ ,% &              @@  .@ .@@@             .,.          @@  %@@    
             %@@@@/        ,@@. % @. @           &@  ,./@@%  *          @.    #@@       .@,  @@    
                /@@@@@@@@@@*  %#  @  / @% ,,*&@(   %@@@.  /&          ..        &@/      @#   *    
              &@&,         %@@    @@  *@.  ./##(,     /@@.            @          @@      @.        
              @@@@@@@@@@@@@(      %@@/   %@@@@@@@@@@@@,               &          #&     @@         
                ,%@@@&(            @@@@(                               @               @@          
                                    /@@@#                               #&          .@@            

"""


frameBR = """
                                                                           (@@@@@#                 
                                                                        @@@@@@%     .              
                                                                      @@@@@,  @@/        @&        
                                                                    #@@@@  %@,              @      
                                                                   #@@@% *@.                 @     
                                                                  ,@@@* &@    *@@*            @    
                                                                  @@@& &@   .@@     &@@@@@/   &    
                                                                 (@@@  @.  %@      &@@@@@@@%  &    
                                                                 @@@( @@  %*       &@@@@@@@% &     
                                                              @  @@@  @* %.         *@@@@@.&       
                                                              @/ @@@  @, *                         
                                                              @@ @@@  @*.           (@@@@@         
                                                              @@ &@@  @&,         @&               
                                                              /@  @@( #@ @@@%   &.                 
                                                               @# &@@  @@@@@@* %                   
                                                                @  @@# @@@@@@@ .                   
                                                                (& *@@  @@@@@@                     
                                                                 @/ &@@  @@@@@#@@@      @@@&(      
                                                                  %  &@& /@@@@@@@@@   @*           
                                                                   #  &@@ /@@@@@@@@# @             
                                                       @@@@@@@@@(   .( #@@ (@@@@@@@&,              
                                                                 (@@( & .@@ %@@@@@@&               
                                                              ,#&&%*  &.  @@ (@@@@@/@@@*           
                                                          &@    *%&%/  .,  @@ (@@@@@@@@@@          
                                                        @&  @@@@@@@@@@@@@*  &@ %@@@@@@@@@@         
                                                       @( &@@@@(      *@@@@@ ,@ (@@@@@@@@@*        
                                                      @@ @@@@ .&@&.       @@@%.@ &@@@@@@@@%        
                                                      @//@@&.@@@@@@@@       @@@.@ @@@@@@@@&        
                                                      @%#@@.&@@@@@@@,&       /@@ @ @@@@@@@(        
                                                      @@ @@& @@@@@@%#@        .@@// @@@@@@         
                                                          @@@,     @@          .@%@ &@@@@@         
                                                            @@@@@@@  *@@@@#     ,@ % @@@@%         
                                                                  (@&       ,@.  @(@ @@@@          
                                                                 @@            @  @* &@@@          
                                                                &@              . @  #@@           
                                                                #*     *@@@@@@@  (&  %@,           
                                                                     #@%     /@@  (. @@  @@@       
              #@@@@@@@@@@@(                                       . @&            /* @   @@@       
          @@@&    (&@@@@%,   *@/             ,        /@@@#      %  &               @   @@@@       
        @@@   @@@@%,   ./@@@@@#  */    @@   %@/    *@@       @   @  (              /(  (@@@#       
      &@@  ,@@(               %@@@  /  %@#  (@#   (@@         \%  \%  &             &/  .@@@%        
     @@#  @@.                     @@@, *%@   @@    .           %  @   /         /&   @@@@,         
    @@%  @@          .,.             @@@. @.  @@              &.%* @#   (@%(%@%    /@@@@           
    @@  ,@.       @@#    .@          *  %@@/.,  @@           @ .@ % .@@,        /@@@@%             
    *   #@      /@&        ..          &/  .@@@%   (@&*,, %@ /  @  #%  *@@@@@@@@@@/                
        .@      @@          @            .@@*     ,(##/.  .@*  @@    @@%         ,&@&              
         @@               &               ,@@@@@@@@@@@@%   /@@%      (@@@@@@@@@@@@@              
          @@               @                               (@@@@            (&@@@%,                
            @@.                                         #@@@/    
"""

frameTR = """
              *@@@@&&@@@.                                                                          
            @@.                                         #@@@(                                    
          @@               @                               (@@@@            (&@@@%,                
         @@               &               ,@@@@@@@@@@@@%   /@@%      (@@@@@@@@@@@@@              
        .@      @@          @            .@@/     ,(##/.  .@*  @@    @@%         ,&@&              
    *   #@      /@&        ..          &/  .@@@%   (@&*,, %@ /  @  #%  *@@@@@@@@@@/                
    @@  ,@.       @@#    .@          *  %@@/.,  @@           @ .@ % .@@,        /@@@@%             
    @@%  @@          .,.             @@@. @.  @@              &.%, @#   (@%(%@%    /@@@@           
     @@#  @@.                     @@@, *%@   @@    .           %  @   /         /&   @@@@,         
      &@@  ,@@(               %@@@  /  %@#  (@#   (@@         \%  \%  &             &/  .@@@%        
        @@@   @@@@%,   ./@@@@@#  */    @@   %@/    *@@       @   @  (              /(  (@@@#       
          &@@&    #&@@@@%,   *@/             *        /@@@#      %  &               @   @@@@       
             .@@@@@@&&&@@@&,                                        @#            ** @  .@@@       
                                                                     #@&     /@@  (. @@  @@@       
                                                                #*     *@@@@@@@  #&  %@,           
                                                                @@              . @  #@@           
                                                                 @@            @  @* &@@@          
                                                                  (@&       ,@.  @(@ @@@@          
                                                            @@@@@@@  *@@@@#     ,@ % @@@@%         
                                                          @@@,     @@          .@%@ &@@@@@         
                                                      @@ @@& @@@@@@%#@        .@@// @@@@@@         
                                                      @%#@@.&@@@@@@@,@       /@@ @ @@@@@@@(        
                                                      @(/@@&.@@@@@@@@       @@@.@ @@@@@@@@&        
                                                      @@ @@@@ .&@&.       @@@%.@ &@@@@@@@@%        
                                                       @( &@@@@(      *@@@@@ ,@ (@@@@@@@@@*        
                                                        @&  @@@@@@@@@@@@@*  &@ %@@@@@@@@@@         
                                                          &@    *%&%/  .,  @@ (@@@@@@@@@@          
                                                              ,#&&%*  &   @@ (@@@@@/@@@*           
                                                                 (@@( & .@@ %@@@@@@&               
                                                       @@@@@@@@@(   ./ #@@ (@@@@@@@&,              
                                                                   #  &@@ /@@@@@@@@# @             
                                                                  \%  \%@& /@@@@@@@@@   @*           
                                                                 &/ &@@  @@@@@#@@@      @@@&(      
                                                                /& *@@  @@@@@@                     
                                                                @  @@( @@@@@@@ .                   
                                                               @# &@@  @@@@@@* %                   
                                                              /@  @@( #@ @@@%   &.                 
                                                              @@ %@@  @&.        .@(               
                                                              @@ @@@  @*.           (@@@@@         
                                                              @/ @@@  @, *                         
                                                              @  @@@  @* %.         *@@@@@.&       
                                                                 @@@( @@  %*       &@@@@@@@% &     
                                                                 (@@@  @.  %@      &@@@@@@@%  &    
                                                                  @@@& &@   .@@     &@@@@@/   &    
                                                                  .@@@* &@    *@@*            @    
                                                                   #@@@% ,@.                 @     
                                                                    #@@@@  %@,              @      
                                                                      @@@@@,  @@/        @&        
                                                                        @@@@@@%     . 
"""

frameTL = """
                                                                           @@@&&@@@@*              
                                    /@@@#                               #&          .@@            
                ,%@@@&(            @@@@(                               @               @@          
              @@@@@@@@@@@@@(      %@@/   %@@@@@@@@@@@@,               &          #&     @@         
              &@&,         %@@    @@  *@.  ./##(,     *@@,            @          @@      @.        
                /@@@@@@@@@@*  %#  @  / @% ,,*&@(   %@@@.  /&          ..        &@/      @#   *    
             %@@@@/        ,@@. % @. @           &@  ,./@@%  *          @.    #@@       .@,  @@    
           @@@@/    %@%(%@(   #@ ,%.&              @@  .@ .@@@             .,.          @@  %@@    
         ,@@@@   &(         /   @  %           .    @@   @%* ,@@@                     .@@  #@@     
        %@@@.  /&             &  \%  \%         @@(   #@(  #@%  /  @@@%               (@@,  @@&      
       #@@@(  (/              (  @   &       @@*    /@%   @@    /*  #@@@@@(.   ,%@@@@   @@@        
       @@@@   @               &  %      #@@@/        ,             /@*   ,#@@@@&(    &@@@          
       @@@.  @ **            %@                                        ,&@@@&&&@@@@@@.             
       @@@  @@ .(  @@/     &@#                                                                     
           ,@%  &(  @@@@@@@*     *%                                                                
           @@#  @ .              @@                                                                
          @@@& *@  @            @@                                                                 
          @@@@ @(@   @,       &@(                                                                  
         %@@@@ % @,     (@@@@*  @@@@@@@                                                            
         @@@@@& @%@.          @@     ,@@@                                                          
         @@@@@@ //@@.        @#%@@@@@@ &@@ @@                                                      
        (@@@@@@@ @ @@/       &,@@@@@@@&.@@#%@                                                      
        &@@@@@@@@ @.@@@       @@@@@@@@.&@@/(@                                                      
        %@@@@@@@@& @.%@@@       .%@&. @@@@ @@                                                      
        *@@@@@@@@@( @, @@@@@*      (@@@@& (@                                                       
         @@@@@@@@@@% @&  *@@@@@@@@@@@@@  @@                                                        
          @@@@@@@@@@( @@  ,.  /%&%*    @&                                                          
           *@@@/@@@@@( @@  .&  *%&,                                                              
               &@@@@@@% @@. & (@@(                                                                 
              ,&@@@@@@@( @@# /.   (@@@@@@@@@                                                       
             & #@@@@@@@@& @@&  #                                                                   
           *@   @@@@@@@@@* &@&  %                                                                  
      (&@@@      @@@#@@@@@  @@& /@                                                                 
                     @@@@@@  @@* &/                                                                
                   . @@@@@@@ (@@  @                                                                
                   % *@@@@@@  @@& #@                                                               
                 .&   %@@@ @# (@@  @/                                                              
               (@.        .&@  @@% @@                                                              
         @@@@@(           .*@  @@@ @@                                                              
                         * ,@  @@@ /@                                                              
       &.@@@@@*          % *@  @@@  @                                                              
     & %@@@@@@@&       *@  @@ (@@@                                                                 
    &  %@@@@@@@&      @%  .@  @@@(                                                                 
    &   /@@@@@&     @@.   @& &@@@                                                                  
    @            *@@*    @& *@@@.                                                                  
     @                 .@* %@@@#                                                                   
      @              ,@%  @@@@%                                                                    
        &@        /@@  ,@@@@@                                                                      
              .     %@@@@@@     
"""

kaotec = """
                                                                                                   
                                         
       .,,,,,,,,,,,,,,,,,,,,/####################,                   */*.                          
       .,,,,,,,,,,,,,,,,,,,,/####################,                 */#(*,.                         
       .,,,,,,,,,,,,,,,,,,,,/####################,              .*(###(*,,,,.                      
       .,,,,,,,,,,,,,,,,,,,,/####################,             *(#####(*,,,,,..                    
       .,,,,,,,.                         (#######,           */######(*,,,,,,,,.                   
       .,,,,,,,.                         /#######,        .,(######/*    .,,,,,,,,.                
       .,,,,,,,.                         /#######,       *(######(*        .,,,,,,,..              
       .,,,,,,,.                         /#######,     ,/######(*.           .,,,,,,,.             
       .,,,,,,,.                         /#######,  .,(######/*                .,,,,,,,,.          
       .,,,,,,,.                         /#######,.*(######(*                    .,,,,,,,..        
       .,,,,,,,.                         /#######((#######*.                       .,,,,,,,.       
       .,,,,,,,.                         /#######,.*#######(,                     ,,,,,,,..        
       .,,,,,,,.                         /#######,  .*#######/,                 ,,,,,,,,.          
       .,,,,,,,.                         /#######,     *(######(,.           .,,,,,,,.             
       .,,,,,,,.                         /#######,       *#######(,         ,,,,,,,..              
       .,,,,,,,.                         /#######,        .*#######/,     ,,,,,,,,.                
       .,,,,,,,.                         (#######,           *(######(,.,,,,,,,.                   
       .,,,,,,,,,,,,,,,,,,,,/####################,             *######(*,,,,,..                    
       .,,,,,,,,,,,,,,,,,,,,/####################,              .*####(*,,,,.                      
       .,,,,,,,,,,,,,,,,,,,,/####################,                 *(#(*,.                         
       .,,,,,,,,,,,,,,,,,,,,/####################,                   */*.                          
                          

"""
def addclassdefs(classdef, font, fontsize):
	dwg.defs.add(dwg.style('.'+classdef+ ' {font-family: '+font+';}'))
	dwg.defs.add(dwg.style('.'+classdef+ ' {font-size: '+str(fontsize)+'px;}'))
	dwg.defs.add(dwg.style('.'+classdef+ ' {white-space: pre; }'))


def printblock(pattern,posx,posy,charscale,charsize, classid, name, font):
	addclassdefs(classid, font, charsize)
	patterndata = pattern.splitlines()
	geopattern = dwg.add(dwg.g(id=name, class_=classid, transform="translate("+str(posx)+","+str(posy)+")"))
	for i,l in enumerate(patterndata):
		newline = ""
		for c in l:
			newline = newline + c	
		geopattern.add(dwg.text(newline, class_=classid, insert=(0,i*charscale*charsize), fill='black'))
	return geopattern




cube = """

	   666666
	  6666661
	 66666611
	666666111
   2222221111
   2222221111
   222222111
   22222211
   2222221

"""
def docube(sp,s1,s2,s3,orientation,size,posx,posy):
	###sp must equal s2 in char length
	cubefontsize = 25
	cube = dwg.add(dwg.g(id="cube", class_="pattern", transform="translate("+str(posx)+","+str(posy)+")"))
	
	for x in xrange(size):
		xline = ""
		space = size
		while space > x:
			xline = xline + sp
			space = space - 1
		side1 = 0
		while side1 < size:
			xline = xline + s1
			side1 = side1 + 1
		side2 = 0
		while side2 < x:
			xline = xline + s2
			side2 = side2 +1
		# xline = xline + "\n"
		print (xline)
		cube.add(dwg.text(xline, class_="pattern", insert=(0,(x*0.7*cubefontsize)), fill='black'))
	for x in xrange(size):
		xline = ""
		side3 = 0
		while side3 < size:
			xline = xline + s3
			side3 = side3 + 1
		side2 = 0
		while side2 < size - x:
			xline = xline + s2
			side2 = side2 + 1
		cube.add(dwg.text(xline, class_="pattern", insert=(0,((size+x)*0.7*cubefontsize)), fill='black'))


# docube("     ","123","piano","321",1,10,0,0)   


######################
###printboxTOP#######
#####################
def printerBoxTop():
	baseoffsetter = 250
	for x in xrange(10):
		doskyline(hollowbox, 450*0.707**x,100+x*100,2,0,0.7**x, True,1)


##########################
### songtext generator ###
###      output        ###
##########################

generatedsongtexts = ["generic my feint represent incidence wishes", "we happening fitting two loon freedom scuba inside a marine colander", "if we survive unable and checkbook refusal decide would we abhorrence singly opponent away the parlance of our acoustics", "forager me inexplicable ensemble and i legacy adolescent shaving bombardment with secret and it testator brook and growth analogy cliff growing from refrigerate that thaw fan it somewhere 2019", "petrify exist the hash and merriment the constitutive to your transplant", "fair the adept reply enigma", "sustenance me solecism pocket", "how highly nostril mandatory triad masculine fetch anterior he feasibility bell humanity holler", "your dungeon pertain guided pass this globe gamut sequester", "if we happen unfamiliar and obtain denial selection would we contempt disjointed polarity away the colloquial of our piano", "if we concurrent halting and acquire abnegation selected would we contempt equivocally otherwise distant the tremolo of our tune", "total my untruth survive often wishes", "i would preferably being a brewery than a blade", "bilingual immigrate unhurried", "antecedent you scapegoat me forfeiture a smug locate yourself", "your culprit reside gait bye this macrocosm perfectly forlorn", "if we inhabit sightless and host objection opt would we acrimony apart diametrical isolated the tremolo of our tune", "if we lifelong undiagnosed and take deny select would we reluctant equivocally inverse asunder the tremolo of our harpsichord", "diet me cryptic inventory", "always of us arrive gloomy assimilation the incomprehensible idealistic knowledge to submarine outlying the astronomical", "nourish me uncanny dancing and i testament maturation fringe occupied with factorize and it recommendation river and growing comparable overeat unaided from west that disband averse it subsist 2019", "if you laugh look me i intestate figuratively inducement that survive something everybody traveled feasibly inwardly the symmetrical colloquialism", "an sincerity lad his mattress occur his peaceful of worried", "ever my cheating represent periodically wishes", "interpreter restitution nonchalant", "language retrieval slow", "if we creature crippled and take inadmissible selective would we contempt individuation opposite outlying the jargon of our soprano", "your arrest occur somnambulism permeable this globe invariably outsider", "an sheer maternal his bedding somewhere his quietude of uneasy", "wholly of us obtain misplaced immersion the shady imagine recitation to port apart the sidereal", "tonal the inventive inquisitor questioning", "an unbiased laddie his rug pertain his pacification of think", "horror populate the scanner and laughing the principal to your bosom", "if you grin look me i tribute understandable beginning that constitute something everybody world act inwardly the equivalent interpreter", "your imprison living biped beyond this immigration stark isolate", "waiver yourselve from psychoanalysis expel zero simply ourselve volition liberty our intentionally", "proportion the virtuoso interrogatory inquire", "forever you must reside morganatic marriage gay extant frequently you request", "nutritional me awkward ballet and i heritage teenage beaver bombardment with insurmountable and it recommendation upstream and unaided predilection stream growing from boreal that fusible comparable it occur 2019", "coordination the outwit demand interrogatory", "if we constitute sight and checkbook inadmissible best would we loathe once inverse separate the jargon of our tune", "we makeup licit two shocked revive pool inmost a roe manger", "hi sir conductor", "your imprison maintenance lope road this internationally everywhere exclusively", "i would perceptibly live a behead than a claw", "antedate you censure me pillage a probation put yourself", "perfect you beg constitute bigamy heterosexual couple here generic you dearth", "your arrest pertain canter porous this macrocosm ever recluse", "your imprisonment coexistence briskly traverse this sightseeing gamut single", "stark my deceptive life frequency wishes", "entirely of us possession disordered indoor the unfathomable reverie recite to motorcycle instead the planetary", "if you gullible inside everlasting farther reincarnation somewhere legitimate a quadruple wednesday lank", "victual me maladroit produce", "separatist yourselve from semiconscious serfdom nothing preliminary ourselve canned gratis our designed", "i whish i procure cringe trample", "if you choice not to adjudicate you immovable procure produce a preferable", "daily creatively incipient reelect from bit inverse inchoate conclude", "former you distrust me acquisition a search entry yourself", "we eternally incidentally two vertigo resuscitated swimmer groove a tuna basket", "lexicographer occur facile", "we abide relevant two puzzled nirvana basketball inward a fishery plumbing", "if you election not to predetermine you tranquil obtain inventor a select", "wholesomeness me unskillful pile", "if you happy site me i able translate arise that eternally something everybody universe act indoors the equal translate", "we stay germane two puzzled phoenix basketball opening a crab receptacle", "if you cuddly nestle me i preparatory interpret stirring that populate something everybody common hyperactive inwardly the homogeneity argot", "if you selected not to ruling you silence fetch fecundity a cull", "predate you incrimination me picking a eye southwest yourself", "how plentitude nose required combined virgin permission previous he box reverberate national howl", "separatist yourselve from crazy secession eleven just ourselve perfectible looseness our worried", "if you determine not to finale you lull grab creativeness a elect", "total my mendacious incident infrequently wishes", "courteously countryman musicologist", "salute platonic performer", "frightening recur the brake and boo the essential to your inhale", "if you selection not to finale you tranquilize take construct a optimum", "dietary me poser pile", "an unbiased bachelor his mantle populate his restful of willfully", "appall abide the decode and jeer the substantial to your lung", "your culprit pertain jump done this planetary forever vacant", "remnant the smart wonder wonder", "if you alternative not to firmness you quiet fetch fabrication a discernment", "invariably you necessity inhabit morganatic sex ex occur everywhere you shortage", "forever my delude happening oft wishes", "if you ponder therein perpetuity thus alive reside legitimate a unpaired dawn steel", "aloha romantic vaudeville", "welcoming sincere theater", "infinitely recent stirring recurring from few polarity trailblazer eventually", "i whish i procure albatross webbed", "entirely of us earn gloomy internal the unintelligible envisage recognize to wheel outdoor the sidereal", "how outnumber auricular ineluctable triad woman approbation prefatory he pile tonic manlike screech", "if you glee treetop me i likely grammarian stirring that recur something everybody all act indoors the equalize idiom", "your felony existence stride transit this cartographer outright isolate", "entirety of us derive perplexed inside the tenebrous psyche rote to submarine facing the observatory", "perfect phony and jovial standing a cousin sound what he hopefully to tonic and education the leftover", "if you menu not to determine you quietly acquire manufacturing a prudence", "forward you rebuke me confiscate a browse plaza yourself", "incessantly my deceive existing frequently wishes", "how substantially crippled need ternary masculine checkbook anterior he tin reverberate nationality whinny", "renewable yourselve from deviance bondage sixteen just ourselve caisson autonomous our concerned", "we makeup scarcely two vertigo metempsychosis scuba upstage a sea sewer", "everywhere falsification and badinage nonviolence a cousin chink what he desideratum to doorbell and crass the debris", "provender me uncanny wad", "horrific outlast the code and merry the indispensability to your auscultation", "wholly you necessary maintenance marriage husband loving somewhere gamut you shortfall", "nutrition me unusual soprano and i codicil inflation otter box with mystery and it likely canal and unaided predilection disgorge ding from boreal that solvent buff it living 2019", "preceding you censure me snatch a fixate put yourself", "if you joviality venue me i preparatory multilingual emanate that living something everybody global voluntary inside the homogeneous vocabulary", "interpreter again slow", "edible me solecism box", "we life mere two powerless dreamer equestrian internal a scad dish", "i would much reside a axe than a harness", "equity the maven questioning why", "pledge husband singer", "generic deceit and exhilaration stationary a cub ring what he covet to click and optimistic the spare", "if you cuddly everywhere me i preliminary enlighten develop that inhabit something everybody worldwide voluntary embedded the equate sentence", "frequently you request survive wife family marry concurrent totally you require", "terror existing the encode and scoff the leading to your tit", "if you predetermine not to resolve you statics property fabrication a selective", "outdistance you irresponsibility me ransack a sideways nestle yourself", "if you exhilaration nearby me i providence empathize arise that inhabit something everybody traveled comport upstage the proportionate word", "equitable the ingenious demand dubious", "nutriment me maladroit commissary", "exude yourselve from amok abolition naught whatever ourselve capability disengage our intentionally", "i whish i belong webbed paw", "total you enough maintenance bigamy marital marital dweller complete you dearth", "if you smiling position me i disinherit figuratively nature that lifelong something everybody locate hasty entree the congruent english", "antedate you censure me snatch a squint find yourself", "i would ravishing creature a distillery than a finger", "weekly initially source along from approximately opposite initial destination", "and inside the conclude the marriage you pillage coexistence evenhanded to the wed you forge", "we life apropos two bewildered resurrect fencing inside a decapod dish", "if you jolly nestle me i likely linguist develop that occur something everybody place volitional inner the equal translation", "precedent you irresponsibility me buccaneer a gaze somewhere yourself", "loosely yourselve from berserk manumission fifteen yet ourselve feasibility gratis our think", "reducing me inscrutable ballet and i bequest develop otter sulfide with unfathomable and it future river and germinate similar creek adult from glacial that oxidize buff it dweller 2019", "i would several existing a brewery than a awl", "spelling recuperate unmolested", "if we concurrent lame and host disclaim prudence would we reluctant varying unshared out the intonation of our music", "if you happy south me i heir translate arise that here something everybody widespread covenant indoors the congruent cant", "how multiplicity auricle ineluctable combined cousin attainable prefatory he caisson chink national croon", "i would moderately subsist a shovel than a sharp", "your conviction existence walk exceed this tour whole isolation", "incessantly of us reach astray aperture the soot visualize comprehend to strategically except the meteorite", "how prosperity auricle duty seven bachelor hold precede he potential ding humankind holler", "we inhabit germane two complicated spirit dive indoors a tuna bath", "intake me poser ensemble and i future growth trim sate with superhuman and it die creek and prosper predilection brook maturity from polar that aqueous predilection it happen 2019", "how lavishly auricular perfunctory ternary virgin acquirement ahead he possibility hearing american gripe", "how lot nose mandatory sextuple ogle incur former he packet sound mankind snivel", "liberation yourselve from cognition confinement zero yet ourselve enable freelance our alarmed", "entire creation embryonic retrieval from few remnant trailblazer expiry", "antedate you reprove me dispossess a show look yourself", "remnant the dextrous curious reply", "invariably my liar creature recidivism wishes", "your arrest eternally hike transcend this transnational invariably recluse", "completely liar and hilarious inert a nephew listen what he envious to hearing and condone the pillow", "consonant return simplification", "and internal the eventually the newlywed you own being consistently to the married you constrain", "fully you necessity reside married loving connubial here generic you insufficiency", "anyhow creation start reelect from least dissent inaugurate finale", "how plentiful auditory require times maternal let ahead he qualification echo continent gripe", "frequently you necessity outlast husband partner fondly living complete you required", "and assimilation the termination the marriage you supplant maintenance equity to the partner you prevarication", "impartiality the sagacity inquiring factorize", "if you decide not to deterministic you quiet procure invention a discernment", "cordially valuable novelist", "guest ma'am solo", "collectively my cheating happening frequently wishes", "an innocence masculine his quilt concurrent his reconciliation of intentionally", "how mellowness crippled obligate integrated guy take formerly he box aloud humankind howling", "and indoors the decease the morganatic you have pertain as to the fiancee you invent", "how lavishly otolaryngology vital three maternal take untimely he pile bell nationality lament", "offset the skilled inquisitive incredulous", "if you ponder inner ever behind reincarnation subsist licit a sextuple tomorrow astride", "fearfulness eternally the firewall and maniacal the underlying to your organ", "endless inaugurate inchoative regain from least polarity initial conclude", "your capture live somnambulism passageway this tour everywhere hermit", "dispassionate the superstar demand solve", "antecedent you irresponsibility me pillage a eye situate yourself", "fatten me inexplicable sonata and i likely grown molt replete with puzzle and it heir beck and stripling indulging gorge growing from antarctica that liquefy funny it live 2019", "your offender occur gait passageway this spaceship wholly separated", "diet me eerie pile", "forever animating outset recover from almost distinction pioneer peroration", "we incident fitting two vertigo resuscitation wrestling inner a decapod trough", "if you menu not to resolved you statics possession fabrication a selection", "completely baloney and jesting halting a masculine sonic what he request to ding and forget the respite", "an straightness gentleman his sheet living his poise of wittingly", "and indoors the moribund the sex you secure here compatible to the wed you inventor", "ingestion me uncanny armory", "nutritional me clumsy inventory", "how profuse head ineluctable ternary macho attainable above he possibility tinkle independence bellow", "absolutely trickery and mockery unchanged a mankind reverberate what he unquenchable to aloud and forget the residual", "liberation yourselve from madden serfdom zero heretofore ourselve possibility complimentary our disturbed", "fatten me inexplicable pack", "if you assume internal unceasingly consequently vitality eternally relevant a ten meditate tolerable", "incessantly you needs eternally honeymoon bigamist marital populate unbroken you necessitate", "and aperture the final the husband you hold abide compatible to the estranged you artificial", "and enclosed the culmination the marry you dispossess populate compare to the partner you generate", "if you joviality locale me i death comprehension incur that inhabit something everybody anywhere hyperactive inland the synchronize french", "previous you bribery me hold a searching hermetically yourself", "entirely cheat and witticism nevertheless a mankind ringing what he yearning to hearing and connive the relaxation", "if you guffaw put me i preamble polyglot emanate that existence something everybody universe practise intramural the coincident french", "alphabet regain shuck", "if you glad position me i testator paraphrase inducement that stay something everybody immanent deed interior the congruent colloquialism", "if you confiding entry perpetually consequently presence exist pertinent a triple monday astride", "unbroken of us earn aghast embedded the night psyche understand to bike distant the telescope", "totally you indispensable exist fondly wife relationship occur complete you beg", "if you snicker south me i likely english incur that extant something everybody countrywide activate absorption the equity linguist", "predecessor you reprove me confiscate a appearance look yourself", "an downright aunt his quilt eternally his liberality of deliberately", "an directness boy his mantle subsist his peaceful of designed", "reducing me enigmatic cram", "i whish i take swan pentameter", "how plentitude nose inevitably thirty brother take formerly he tinplate hearing civilian shout", "lexicographer recuperate nonchalant", "unlimited innovative initiative along from slightly contrastingly inchoative culminate", "stark cheat and jesting idleness a aunt tonic what he aspire to tocsin and flatten the residual", "continued begin origin reach from smattering etcetera launch coda", "fair the dextrous nosy factorize", "vitamin me sibylline wad", "if you contemplate aperture perpetual retrospective humankind inhabit pertinent a once tuesday athwart", "totally baloney and joggle inert a aunt telephone what he fortunate to tocsin and undeserved the survivor", "underling yourselve from semiconscious cancellation undress still ourselve steel complimentary our intentional", "completely my dissimulation outlast ever wishes", "how affluent auricular mandatory united lad regain preview he competent telephone national wail", "liberation yourselve from demoniac captivity eleven only ourselve qualification unofficial our designed", "pronunciation immigrate handy", "nigger yourselve from hallucinate monarchy fortnight notwithstanding ourselve canned leeway our wittingly", "i would little dwell a blacksmith than a clipper", "outright of us arrive helpless within the unaccountable reverie familiarization to strategically separately the astronomer", "liberally yourselve from mentally nigger everywhere just ourselve perfectible renewable our thoughtful", "your incarcerate populate stride finished this sightseeing complete solely", "unfettered yourselve from alertness serfdom thirteen hitherto ourselve crucible unfettered our nervous", "every fake and buffoonery pacific a brother clang what he unquenchable to phonic and unconcerned the dormancy", "forager me enigmatic accumulate", "nutrition me odd cantata and i preliminary puberty whiskered barrage with recondite and it impulsion beck and thrive indistinguishable gorge puberty from boreal that hydrate buff it live 2019", "frighten live the net and laughing the principal to your pancreas", "if you chosen not to selection you complacency checkbook fabricate a optimum", "complete of us secure hopeless indoors the shadowy daydream comprehend to overindulgence outdoors the galaxy", "if you infer inward changeless so outlive exist fitting a reunify midnight patient", "discharge yourselve from psychology manacle seventeen indignity ourselve confidently illimitable our dejection", "if you assuming included ceaseless shortly creature abide seemly a trio darkness podium", "your prisoner lifelong climbing elapse this multinational complete exclusively", "i would roughly survive a liquor than a abrade", "we eternally coincidentally two powerless paradise bathing position a seahorse hay", "an naivete boy his rug here his rapprochement of uneasy", "and opening the ending the marital you deprive outlast evenhanded to the marital you generate", "how richness nose perfunctory trinity bachelor take precede he shelf loudly manlike growl", "we here pertinent two aghast disbelieve bathing indoors a roach mortar", "your felony happen pace seep this traveler wholly solely", "greeting lovely song", "petrify dweller the net and uproarious the importantly to your organ", "an sheer mankind his mat eternally his quietly of wittingly", "fully my treacherous concurrent constantly wishes", "i whish i approbation chicken horseshoe", "unencumbered yourselve from vigilance colonize nil simply ourselve confidently unencumbered our afraid", "aloha seduce pianist", "an directness boyfriend his berth populate his pacific of concerned", "perpetual creatively start retrieval from around opposite start peroration", "whole my fraudulent maintenance sometimes wishes", "phobia recur the hieroglyph and laughing the importantly to your kidney", "if we dweller undetected and own controvert circumspection would we dislike both dissent apart the parlance of our megaphone", "an truthfulness macho his rest occur his concord of headed", "precedent you castigation me ransack a fixate nestle yourself", "if we survive cripple and possessor defense scarify would we misogyny seriatim otherwise away the stammer of our octave", "intimidate existence the breaking and banter the prime to your respiration", "whole you must subsist husband fiancee newlywed creature collectively you entreat", "i would partially creature a behead than a harness", "your dungeon extant canter bye this macrocosm altogether isolate", "your intern occur hike cross this earth every loneliness", "your prisoner recur jogging along this universe collectively outsider", "if you grin in me i codicil realize arise that living something everybody immanent activity inward the equivalent argot", "if we constitute cripple and proprietor denial reelect would we abomination idiosyncratic antithetical remote the inflect of our contralto", "client friendship conductor", "politely brethren solo", "frequently of us regain astray immersion the black fancied erudition to wheel outpost the planetarium", "if you abstention not to resolve you nevertheless holder imagination a scarify", "i whish i acquire pusillanimous ungulate", "customer paramour studio", "an unbiased virgin his blanket here his quietness of distressed", "if we survive disabled and own refutable selective would we contempt another inverse secluded the colloquialism of our ballad", "term recover untroubled", "i whish i let boggle flipper", "unofficial yourselve from cognition revocation exposed preliminary ourselve likely gratis our intentional", "and enclosed the extremity the suitor you usurp recur twin to the family you fecundity", "dictionary staircase lope", "salute madam stunt", "how plenteous sniff oblige oneness cousin retention priority he likely noise chieftain wail", "i whish i acquire spoonbill cloven", "fully you indispensability maintenance heterosexual family ex subsist totally you crave", "i whish i attainable shrink fin", "symmetry the artfully curiosity questioning", "liberate yourselve from lunatic bondage somewhere preliminary ourselve preferably emancipation our purposely", "vocabulary recuperate unhurried", "stark of us bring perplexed within the fading fancied empathetic to port solitary the cosmos", "aloha platonic vaudeville", "horror dwell the net and joke the substantive to your spleen", "greet adore guitar", "if you happy locate me i future paraphrase grounds that dweller something everybody universal indulge inmost the alike dictionary", "i whish i property spoonbill wheelchair"]

#######################
### whoyougonnacall####
#######################

if printerBoxFrontPanel:
	dwg = svgwrite.Drawing('printerBoxFront.svg', size=("600mm","400mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),("600mm","400mm"), fill="grey"))
	printerBoxFront()
	dwg.save()

if printerBoxSidePanel:
	dwg = svgwrite.Drawing('printerBoxSide.svg', size=("400mm","410mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),("400mm","410mm"), fill="grey"))
	printerBoxSide()
	dwg.save()

if printerBoxTopPanel:
	dwg = svgwrite.Drawing('printerBoxTop.svg', size=("500mm","400mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),("500mm","400mm"), fill="grey"))
	printerBoxTop()
	dwg.save()

####piano####

if pianoCoverInsidePanel:
	print(str(pianoCoverInsidePanelSize[0])+"mm",str(pianoCoverInsidePanelSize[1])+"mm")
	dwg = svgwrite.Drawing('6b_pianoCoverInside.svg', size=(str(pianoCoverInsidePanelSize[0])+"mm",str(pianoCoverInsidePanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoCoverInsidePanelSize[0])+"mm",str(pianoCoverInsidePanelSize[1])+"mm"), fill="grey"))
	emocrowd(0,50,False)
	dwg.save()

if pianoCoverOutsidePanel:
	dwg = svgwrite.Drawing('6a_pianoCoverOutside.svg', size=(str(pianoCoverOutsidePanelSize[0])+"mm",str(pianoCoverOutsidePanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoCoverOutsidePanelSize[0])+"mm",str(pianoCoverOutsidePanelSize[1])+"mm"), fill="grey"))
	emocrowd(0,50,True)
	dwg.save()

if pianoBottomPanel:
	dwg = svgwrite.Drawing('7_pianoBottom.svg', size=(str(pianoBottomPanelSize[0])+"mm",str(pianoBottomPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBottomPanelSize[0])+"mm",str(pianoBottomPanelSize[1])+"mm"), fill="grey")) 	
	rotationdots(300,600)
	dwg.save()

if pianoFrontPanel:
	dwg = svgwrite.Drawing('5_pianoFront.svg', size=(str(pianoFrontPanelSize[0])+"mm",str(pianoFrontPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoFrontPanelSize[0])+"mm",str(pianoFrontPanelSize[1])+"mm"), fill="grey"))
		dwg.add(dwg.rect(("40mm","70mm"),("110mm","150mm"), fill="red"))

	
	# emocrowd(0,50,False)
	# dwg.defs.add(dwg.style('.block {font-family: Wonky Pins;}'))
	printblock(circuit,2600,10,1,9,"circuit2", "circuit2","Courier")
	# dwg.defs.add(dwg.style('.block {font-family: Courier;}'))
	# dwg.defs.add(dwg.style('.block {font-size: '+str(pianoFrontFontsize)+'px;}'))
	# dwg.defs.add(dwg.style('.block {white-space: pre; }'))
	# river2(300,1500,50,25,-0.55,1,generatedsongtexts)
	river2(50,1500,50,25,-0.55,1,generatedsongtexts)
	river2(48,3200,50,0,2.1,1,generatedsongtexts)

	printblock(instructions,1050,500,1,20,"instructions", "instructions","Courier")
	printblock(tweetperson, 750,300,1,20,"tweetperson", "tweetperson","Courier")
	printblock(rtfm, 800,60,1,20,"rtfm", "rtfm","Courier")
	printblock(nfo,4000,0,1,9.5,"nfo", "nfo","Courier")
	printblock(frameTL,10,170,1,5,"frame0","frame","Courier")
	printblock(frameTR,410,170,1,5,"frame1","frame","Courier")
	printblock(frameBL,10,660,1,5,"frame2","frame","Courier")
	printblock(frameBR,410,660,1,5,"frame3","frame","Courier")
	# printblock(kaotec,750,780,1,10,"kaoetc","kaotec","Courier")
	dwg.save()


if pianoTopPanel:
	dwg = svgwrite.Drawing('4_pianoTop.svg', size=(str(pianoTopPanelSize[0])+"mm",str(pianoTopPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoTopPanelSize[0])+"mm",str(pianoTopPanelSize[1])+"mm"), fill="grey"))
	river(300,5500,300,90,1,strategies)
	# patternsetdefs()
	# patternstudy(10, False)
	dwg.save()

####pianobox

if pianoBoxLeftPanel:
	dwg = svgwrite.Drawing('8_pianoBoxLeft.svg', size=(str(pianoBoxLeftPanelSize[0])+"mm",str(pianoBoxLeftPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxLeftPanelSize[0])+"mm",str(pianoBoxLeftPanelSize[1])+"mm"), fill="grey"))
	patternsetdefs()
	patternstudy(10, False, True)
	dwg.save()

if pianoBoxRightPanel:
	dwg = svgwrite.Drawing('10_pianoBoxRight.svg', size=(str(pianoBoxRightPanelSize[0])+"mm",str(pianoBoxRightPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxRightPanelSize[0])+"mm",str(pianoBoxRightPanelSize[1])+"mm"), fill="grey"))
	patternsetdefs()
	multigeopattern(40,1600,5000,False)
	dwg.save()

if pianoBoxBackPanel:
	dwg = svgwrite.Drawing('3_pianoBoxBack.svg', size=(str(pianoBoxBackPanelSize[0])+"mm",str(pianoBoxBackPanelSize[1])+"mm"), profile='full')
	debugdefs()
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxBackPanelSize[0])+"mm",str(pianoBoxBackPanelSize[1])+"mm"), fill="grey"))
	skylinedefs()
	doskyline(skyline, 0, 400,2,0,1,1,1)
	clouddefs()
	multibottomcloud(3,afxtracks[1], 100,100)
	multibottomcloud(3,afxtracks[2], 1000,200)
	multibottomcloud(4,afxtracks[3], 2500,400)
	multibottomcloud(3,afxtracks[4], 1500,100)
	multibottomcloud(2,afxtracks[5], 3100,200)
	multibottomcloud(3,afxtracks[6], 3500,200)
	multibottomcloud(5,afxtracks[7], 4500,400)
	multibottomcloud(3,afxtracks[8], 5200,100)
	dwg.save()

if pianoBoxBackPanelSmall:
	dwg = svgwrite.Drawing('3_pianoBoxBackSmall.svg', size=(str(pianoBoxBackPanelSmallSize[0])+"mm",str(pianoBoxBackPanelSmallSize[1])+"mm"), profile='full')
	debugdefs()
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxBackPanelSmallSize[0])+"mm",str(pianoBoxBackPanelSmallSize[1])+"mm"), fill="grey"))
	skylinedefs()
	skylinefontsize = 22
	doskyline(skyline, 0, 400,2,0,1,0,1)
	# doskyline(skyline, posx, posy, charscale, rot, scale, rand, vertskyscale)
	clouddefs()
	multibottomcloud(3,afxtracks[1], 100,100)
	multibottomcloud(3,afxtracks[2], 1000,200)
	multibottomcloud(4,afxtracks[3], 2500,400)
	multibottomcloud(3,afxtracks[4], 1500,100)
	multibottomcloud(2,afxtracks[5], 3100,200)
	multibottomcloud(3,afxtracks[6], 3500,200)
	multibottomcloud(5,afxtracks[7], 4500,400)
	multibottomcloud(3,afxtracks[8], 5200,100)
	dwg.save()

if pianoBoxTopPanel:
	dwg = svgwrite.Drawing('2_pianoBoxTop.svg', size=(str(pianoBoxTopPanelSize[0])+"mm",str(pianoBoxTopPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxTopPanelSize[0])+"mm",str(pianoBoxTopPanelSize[1])+"mm"), fill="grey"))
	pianoBoxTop()
	dwg.save()

if pianoBoxFrontPanel:
	dwg = svgwrite.Drawing('1_pianoBoxFront.svg', size=(str(pianoBoxFrontPanelSize[0])+"mm",str(pianoBoxFrontPanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxFrontPanelSize[0])+"mm",str(pianoBoxFrontPanelSize[1])+"mm"), fill="grey"))
	# patternsetdefs()
	# multigeopattern(40,1600,5000,False)
	pianoBoxFront()
	dwg.save()


if pianoBoxLeftTrianglePanel:
	dwg = svgwrite.Drawing('9_pianoBoxLeftTriangle.svg', size=(str(pianoBoxLeftTrianglePanelSize[0])+"mm",str(pianoBoxLeftTrianglePanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxLeftTrianglePanelSize[0])+"mm",str(pianoBoxLeftTrianglePanelSize[1])+"mm"), fill="grey"))
	dwg.defs.add(dwg.style('.feeder {font-family: Wonky Pins;}'))
	dwg.defs.add(dwg.style('.feeder {font-size: '+str(printerboxfontsize)+'px;}'))
	dwg.defs.add(dwg.style('.feeder {white-space: pre; }'))
	for x in xrange(10):
		doskyline(hollowbox, 500+450*-0.807**x,-100+x*200,2,0,0.7**x, True,1)
		doskyline(hollowbox, 1700+450*0.707**x,0+x*200,4,45,0.7**x, True,1)
	dwg.save()

if pianoBoxRightTrianglePanel:
	dwg = svgwrite.Drawing('11_pianoBoxRightTriangle.svg', size=(str(pianoBoxRightTrianglePanelSize[0])+"mm",str(pianoBoxRightTrianglePanelSize[1])+"mm"), profile='full')
	if debug:
		dwg.add(dwg.rect(("0mm","0mm"),(str(pianoBoxRightTrianglePanelSize[0])+"mm",str(pianoBoxRightTrianglePanelSize[1])+"mm"), fill="grey"))
	# dwg.defs.add(dwg.style('.feeder {font-family: Courier;}'))
	# dwg.defs.add(dwg.style('.feeder {font-size: '+str(printerboxfontsize)+'px;}'))
	# dwg.defs.add(dwg.style('.feeder {white-space: pre; }'))
	feederdefs()
	feedmeweirdmusic(2850,50,90, True)
	dwg.save()