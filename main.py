from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.properties import Clock
from kivy.properties import NumericProperty
from kivy.metrics import dp
from kivy.core.audio import SoundLoader

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class cancelHelp:
    def cancel(self):
        pass

class MainWidget(BoxLayout):
    beatnext=cancelHelp()
    d=1
    playing=False
    def __init__(self, **kw):
        self.orientation='vertical'
        super().__init__(**kw)

        # Initializing the sounds

        self.cracksound=SoundLoader.load('crack.mp3')
        self.cracksound.volume=0.3
        self.drumsound=SoundLoader.load('drum.mp3')
        self.shootsound=SoundLoader.load('shoot.mp3')
        self.shootsound.volume=0.3
        self.clapsound=SoundLoader.load('clap.mp3')
        self.clapsound.volume=0.2
        self.clicksound=SoundLoader.load('click.mp3')
        self.clicksound.volume=0.4
        self.cymbalsound=SoundLoader.load('cymbal.mp3')

        self.crsvol=self.cracksound.volume/100
        self.drsvol=self.drumsound.volume/100
        self.shsvol=self.shootsound.volume/100
        self.clsvol=self.clapsound.volume/100
        self.clisvol=self.clicksound.volume/100
        self.cysvol=self.cymbalsound.volume/100

        # Adding the upper box layout for Skipper beat label and speed and volume control

        self.upbox=BoxLayout(size_hint=(1, .2))
        
        'Skipper beat label'

        self.upbox.add_widget(Label(text="S : K : I : P : P : E : R   B : E : A : T", font_size=dp(30), size_hint=(0.6, 1)))

        'Adding Pause/Play Button'

        self.ppbutton=ToggleButton(text='Paused', size_hint=(0.12, 0.6), pos_hint={'center_y':0.5, 'left':0})
        self.ppbutton.bind(state=self.pauseplay)

        self.upbox.add_widget(self.ppbutton)

        'Defining Speed Slider, Label and BoxLayout for speed'

        self.speedslide=Slider(min=0, max=100)

        self.speedlabel=Label(text="Speed: 100")

        self.speedbox=BoxLayout(orientation='vertical', size_hint=(.5, 0.7), pos_hint={'center_y':0.5})

        self.speedbox.add_widget(self.speedlabel)


        self.speedslide.bind(value=self.on_value_speed)

        self.speedslide.value_track=True
        self.speedslide.step=5
        self.speedslide.value=0
        self.speedslide.value_track_color=[0, 1, 0, 1] 

        self.speedbox.add_widget(self.speedslide)

        self.upbox.add_widget(self.speedbox)

        'Defining Volume Slider, Label and BoxLayout for Volume'

        self.volslide=Slider(min=0, max=100)
        self.vollabel=Label(text='Volume:100')

        self.volbox=BoxLayout(orientation='vertical', size_hint=(.5, 0.7), pos_hint={'center_y':0.5})
        self.volbox.add_widget(self.vollabel)


        self.volslide.bind(value=self.on_value_volume)

        self.volslide.value_track=True
        self.volslide.step=1
        self.volslide.value=100
        self.volslide.value_track_color=[1, 0, 0, 1]

        self.volbox.add_widget(self.volslide)

        self.upbox.add_widget(self.volbox)

        'Adding the Upper BoxLayout on the screen'

        self.add_widget(self.upbox)

        # Adding the second box layout for beat bar

        'Defining BoxLayout'

        self.midbox=BoxLayout(size_hint=(1, .1))
        
        'Adding spaces'

        self.midbox.add_widget(Label())
        self.midbox.add_widget(Label())

        'Adding Beat Locator buttons'

        self.beat1=Button(text=' ',
        disabled=False,
        background_color=(0.4, 1, 0.4, 1),
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat1)
        self.beat2=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat2)
        self.beat3=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat3)
        self.beat4=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat4)
        self.beat5=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat5)
        self.beat6=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat6)

        self.speed=NumericProperty()
        self.speed=1-(self.speedslide.value/100)

        self.beatnext=Clock.schedule_interval(self.nextbeatplay, self.speed*self.d)
        self.speedslide.value=75

        # Will add More if more rows are added
        
        '''self.beat7=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat7)
        self.beat8=Button(text=' ',
        disabled=True,
        size_hint=(1, .1))
        self.midbox.add_widget(self.beat8)'''

        'Adding Last space'

        self.midbox.add_widget(Label())

        'Adding The Middle Box Layout To Screen'

        self.add_widget(self.midbox)

        # Adding the 3rd box layout for Beats and Toggle Buttons

        'Defining BoxLayout'

        self.lowerbox=BoxLayout()

        'Adding beat label BoxLayout'

        self.bllayout=BoxLayout(orientation='vertical', size_hint=(1, 0.95))

        self.bllayout.add_widget(Label(text='   C y m b a l', font_size=20))
        self.bllayout.add_widget(Label(text='   D r u m', font_size=20))
        self.bllayout.add_widget(Label(text='   C l a p', font_size=20))
        self.bllayout.add_widget(Label(text='   C l i c k', font_size=20))
        self.bllayout.add_widget(Label(text='   S h o o t', font_size=20))
        self.bllayout.add_widget(Label(text='   C r a c k', font_size=20))
        self.lowerbox.add_widget(self.bllayout)

        'Adding row 1'

        self.bsr1=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal1=ToggleButton()
        self.bsr1.add_widget(self.cymbal1)
        self.drum1=ToggleButton()
        self.bsr1.add_widget(self.drum1)
        self.clap1=ToggleButton()
        self.bsr1.add_widget(self.clap1)
        self.click1=ToggleButton()
        self.bsr1.add_widget(self.click1)
        self.shoot1=ToggleButton()
        self.bsr1.add_widget(self.shoot1)
        self.crack1=ToggleButton()
        self.bsr1.add_widget(self.crack1)

        self.lowerbox.add_widget(self.bsr1)

        print(self.cymbal1.color)

        'Adding row 2'

        self.bsr2=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal2=ToggleButton()
        self.bsr2.add_widget(self.cymbal2)
        self.drum2=ToggleButton()
        self.bsr2.add_widget(self.drum2)
        self.clap2=ToggleButton()
        self.bsr2.add_widget(self.clap2)
        self.click2=ToggleButton()
        self.bsr2.add_widget(self.click2)
        self.shoot2=ToggleButton()
        self.bsr2.add_widget(self.shoot2)
        self.crack2=ToggleButton()
        self.bsr2.add_widget(self.crack2)
        
        self.lowerbox.add_widget(self.bsr2)

        'Adding row 3'

        self.bsr3=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal3=ToggleButton()
        self.bsr3.add_widget(self.cymbal3)
        self.drum3=ToggleButton()
        self.bsr3.add_widget(self.drum3)
        self.clap3=ToggleButton()
        self.bsr3.add_widget(self.clap3)
        self.click3=ToggleButton()
        self.bsr3.add_widget(self.click3)
        self.shoot3=ToggleButton()
        self.bsr3.add_widget(self.shoot3)
        self.crack3=ToggleButton()
        self.bsr3.add_widget(self.crack3)
        
        self.lowerbox.add_widget(self.bsr3)

        'Adding row 4'

        self.bsr4=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal4=ToggleButton()
        self.bsr4.add_widget(self.cymbal4)
        self.drum4=ToggleButton()
        self.bsr4.add_widget(self.drum4)
        self.clap4=ToggleButton()
        self.bsr4.add_widget(self.clap4)
        self.click4=ToggleButton()
        self.bsr4.add_widget(self.click4)
        self.shoot4=ToggleButton()
        self.bsr4.add_widget(self.shoot4)
        self.crack4=ToggleButton()
        self.bsr4.add_widget(self.crack4)
        
        self.lowerbox.add_widget(self.bsr4)

        'Adding row 5'

        self.bsr5=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal5=ToggleButton()
        self.bsr5.add_widget(self.cymbal5)
        self.drum5=ToggleButton()
        self.bsr5.add_widget(self.drum5)
        self.clap5=ToggleButton()
        self.bsr5.add_widget(self.clap5)
        self.click5=ToggleButton()
        self.bsr5.add_widget(self.click5)
        self.shoot5=ToggleButton()
        self.bsr5.add_widget(self.shoot5)
        self.crack5=ToggleButton()
        self.bsr5.add_widget(self.crack5)
        
        self.lowerbox.add_widget(self.bsr5)

        'Adding row 6'

        self.bsr6=BoxLayout(orientation='vertical', size_hint=(0.5, 0.95))

        self.cymbal6=ToggleButton()
        self.bsr6.add_widget(self.cymbal6)
        self.drum6=ToggleButton()
        self.bsr6.add_widget(self.drum6)
        self.clap6=ToggleButton()
        self.bsr6.add_widget(self.clap6)
        self.click6=ToggleButton()
        self.bsr6.add_widget(self.click6)
        self.shoot6=ToggleButton()
        self.bsr6.add_widget(self.shoot6)
        self.crack6=ToggleButton()
        self.bsr6.add_widget(self.crack6)
        
        self.lowerbox.add_widget(self.bsr6)

        # Will Add More Rows If Needed

        '''Adding row 7'

        self.bsr1=BoxLayout(orientation='vertical', size_hint=(0.95, 1))


        
        self.lowerbox.add_widget(self.bsr1)

        'Adding row 8'

        self.bsr1=BoxLayout(orientation='vertical', size_hint=(0.95, 1))


        
        self.lowerbox.add_widget(self.bsr1)'''

        'Adding space'

        self.lowerbox.add_widget(Label(size_hint=(0.5, 1)))

        'Adding Lower BoxLayout To screen'

        self.add_widget(self.lowerbox)

        Clock.schedule_interval(self.setbeatzero, .05)

    def setbeatzero(self, dt):
        if not self.playing:
            if not self.beat2.disabled:
                self.beat2.background_color=(1, 1, 1, 1)
                self.beat2.disabled=True
                self.beat1.background_color=(0, 1, 0, 1)
                self.beat1.disabled=False
            elif not self.beat3.disabled:
                self.beat3.background_color=(1, 1, 1, 1)
                self.beat3.disabled=True
                self.beat1.background_color=(0, 1, 0, 1)
                self.beat1.disabled=False
            elif not self.beat4.disabled:
                self.beat4.background_color=(1, 1, 1, 1)
                self.beat4.disabled=True
                self.beat1.background_color=(0, 1, 0, 1)
                self.beat1.disabled=False
            elif not self.beat5.disabled:
                self.beat5.background_color=(1, 1, 1, 1)
                self.beat5.disabled=True
                self.beat1.background_color=(0, 1, 0, 1)
                self.beat1.disabled=False
            elif not self.beat6.disabled:
                self.beat6.background_color=(1, 1, 1, 1)
                self.beat6.disabled=True
                self.beat1.background_color=(0, 1, 0, 1)
                self.beat1.disabled=False
        
    def on_value_speed(self, instance, speed):
        self.speed=(100-speed)/100
        self.speedlabel.text=f"Speed: {int(speed)}%"
        self.beatnext.cancel()
        if self.playing:
            self.beatnext=Clock.schedule_interval(self.nextbeatplay, self.speed)
        if speed>=66:
            self.speedslide.value_track_color=[0, 1, 0, 1]
        elif speed>=33:
            self.speedslide.value_track_color=[0, 1, 0.8, 1] 
        else:
            self.speedslide.value_track_color=[0.3, 0.6, 1, 1]

    def on_value_volume(self, instance, volume):
        self.vollabel.text=f"Volume: {int(volume)}%"
        if volume>=66:
            self.volslide.value_track_color=[1, 0, 0, 1] 
        elif volume>=33:
            self.volslide.value_track_color=[0.8, 1, 0, 1] 
        else:
            self.volslide.value_track_color=[0, 0.6, 0.3, 1] 

        self.drumsound.volume=self.drsvol*volume
        self.cymbalsound.volume=self.cysvol*volume
        self.clapsound.volume=self.clsvol*volume
        self.clicksound.volume=self.clisvol*volume
        self.shootsound.volume=self.shsvol*volume
        self.cracksound.volume=self.crsvol*volume

    def nextbeatplay(self, dt):
        self.d=dt*self.speed
        self.beatnext.cancel()
        if self.playing:
            self.beatnext=Clock.schedule_interval(self.nextbeatplay, self.speed)
        if not self.beat1.disabled:
            self.beat1.background_color=(1, 1, 1, 1)
            self.beat1.disabled=True
            self.beat2.background_color=(0, 1, 0, 1)
            self.beat2.disabled=False
            if self.drum2.state=='down':
                self.drumsound.play()
            if self.crack2.state=='down':
                self.cracksound.play()
            if self.shoot2.state=='down':
                self.shootsound.play()
            if self.clap2.state=='down':
                self.clapsound.play()
            if self.click2.state=='down':
                self.clicksound.play()
            if self.cymbal2.state=='down':
                self.cymbalsound.play()
        elif not self.beat2.disabled:
            self.beat2.background_color=(1, 1, 1, 1)
            self.beat2.disabled=True
            self.beat3.background_color=(0, 1, 0, 1)
            self.beat3.disabled=False
            if self.drum3.state=='down':
                self.drumsound.play()
            if self.crack3.state=='down':
                self.cracksound.play()
            if self.shoot3.state=='down':
                self.shootsound.play()
            if self.clap3.state=='down':
                self.clapsound.play()
            if self.click3.state=='down':
                self.clicksound.play()
            if self.cymbal3.state=='down':
                self.cymbalsound.play()
        elif not self.beat3.disabled:
            self.beat3.background_color=(1, 1, 1, 1)
            self.beat3.disabled=True
            self.beat4.background_color=(0, 1, 0, 1)
            self.beat4.disabled=False
            if self.drum4.state=='down':
                self.drumsound.play()
            if self.crack4.state=='down':
                self.cracksound.play()
            if self.shoot4.state=='down':
                self.shootsound.play()
            if self.clap4.state=='down':
                self.clapsound.play()
            if self.click4.state=='down':
                self.clicksound.play()
            if self.cymbal4.state=='down':
                self.cymbalsound.play()
        elif not self.beat4.disabled:
            self.beat4.background_color=(1, 1, 1, 1)
            self.beat4.disabled=True
            self.beat5.background_color=(0, 1, 0, 1)
            self.beat5.disabled=False
            if self.drum5.state=='down':
                self.drumsound.play()
            if self.crack5.state=='down':
                self.cracksound.play()
            if self.shoot5.state=='down':
                self.shootsound.play()
            if self.clap5.state=='down':
                self.clapsound.play()
            if self.click5.state=='down':
                self.clicksound.play()
            if self.cymbal5.state=='down':
                self.cymbalsound.play()
        elif not self.beat5.disabled:
            self.beat5.background_color=(1, 1, 1, 1)
            self.beat5.disabled=True
            self.beat6.background_color=(0, 1, 0, 1)
            self.beat6.disabled=False
            if self.drum6.state=='down':
                self.drumsound.play()
            if self.crack6.state=='down':
                self.cracksound.play()
            if self.cymbal6.state=='down':
                self.cymbalsound.play()
            if self.shoot6.state=='down':
                self.shootsound.play()
            if self.clap6.state=='down':
                self.clapsound.play()
            if self.click6.state=='down':
                self.clicksound.play()
        elif not self.beat6.disabled:
            self.beat6.background_color=(1, 1, 1, 1)
            self.beat6.disabled=True
            self.beat1.background_color=(0, 1, 0, 1)
            self.beat1.disabled=False
            if self.drum1.state=='down':
                self.drumsound.play()
            if self.cymbal1.state=='down':
                self.cymbalsound.play()
            if self.clap1.state=='down':
                self.clapsound.play()
            if self.crack1.state=='down':
                self.cracksound.play()
            if self.click1.state=='down':
                self.clicksound.play()
            if self.shoot1.state=='down':
                self.shootsound.play()

    def pauseplay(self, a, b):
        if self.ppbutton.state=='down':
            self.ppbutton.text='Playing'
            self.playing=True
            self.beatnext.cancel()
            self.beatnext=Clock.schedule_interval(self.nextbeatplay, self.speed)
        else:
            self.ppbutton.text='Paused'
            self.playing=False

MainApp().run()