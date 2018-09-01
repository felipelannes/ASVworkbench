from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import RegexValidator



# Create your models here.

#class NAME(models.Model):
	#Relations
	#Attributes - Mandatory
	#Attributes - Optional
	#Object Manager
	#Custom Properties
	#Dunders
	#Methods
	#Meta and String

class MASS_PROPERTY(models.Model):

	'''
		@quais metadados ainda poderiam ser adicionados aqui. Refletir Mass_Property do SolidWorks

	'''
	
	#Relations
	#Attributes - Mandatory
	#id = models.AutoField(primary_key=True)
	mass = models.DecimalField('Mass', max_digits=13, decimal_places=3,null=True, help_text="in kg")
	lcg = models.DecimalField('LCG', max_digits=6, decimal_places=3,null=True, help_text="in m")
	tcg = models.DecimalField('TCG', max_digits=6, decimal_places=3,null=True, help_text="in m")
	vcg = models.DecimalField('VCG', max_digits=6, decimal_places=3,null=True, help_text="in m")
	#Should be BigIntergerField ??? 
	ixx = models.DecimalField('Ixx', max_digits=12, decimal_places=3,null=True, help_text="in kg·m²")
	iyy = models.DecimalField('Iyy', max_digits=12, decimal_places=3,null=True, help_text="in kg·m²")
	izz = models.DecimalField('Izz', max_digits=12, decimal_places=3,null=True, help_text="in kg·m²")


	#Attributes - Optional
	#Object Manager
	#Custom Properties
	#Dunders
	#Methods
	
	#Meta
	class Meta:
		verbose_name = 'Mass Property'
		verbose_name_plural = 'Mass Properties'
		ordering=['-mass']
		abstract = True



class VESSEL(MASS_PROPERTY):

    #Relations
    #created_by = models.ForeignKey('auth.User', default=request.user)


    #Attributes - Mandatory
	id = models.AutoField(primary_key=True)
	project_number = models.CharField(
		'ASV Project Number',
		max_length=4,
		validators=[RegexValidator(regex=r'^[A-Z0-9]+$')],
		unique=True)
	name = models.CharField('Name',max_length=32,unique=True)
	description = models.TextField('Description',blank=True)
    ####################### MASS PROPERTIES FROM ABSTRACT CLASS  #################################


    #Attributes - Optional
	slug = models.SlugField('slug',unique=True)
	image = models.ImageField(
        upload_to='img/vessel/cover', verbose_name='Vessel Image',
        null=True, blank=True
    )
	created_at = models.DateTimeField('Created at', auto_now_add=True)
	modified_at = models.DateTimeField('Modified at', auto_now=True)

    

    #Object Manager
    #Custom Propreties

    #Dunders
	def __str__(self):
		return '{:s} '.format(self.name)

	def __repr__(self):
		return 'ASV Project Number: {:s} '.format(self.project_number)

    #Methods
	def get_absolute_url(self):
		return reverse('vessel-detail',kwargs={'slug':self.slug})

	def project_number_normalization(self):
		self.project_number = self.project_number.capitalize()

	def calculate_mass(self):
		self.mass = VESSEL.objects.all()
	
	#Meta
	class Meta:
		verbose_name = 'Vessel'
		verbose_name_plural = 'Vessel'
		ordering = ['-created_at'] #rethink this ordering
        #unique_together=('ASV_Project_Number','Name')


class PART(MASS_PROPERTY):
	'''
		One part can have one or mutiplus items. So, the mass property is relative to the part.
	'''
	#constant
	GROUP_SYSTEM_CHOICE = (
			(100,'Structure'),
			(200,'Propulsion'),
			(300,'Eletrical'),
			(400,'Control'),
			(500,'Auxiliary System'),
			(600,'Outfit'),
			(700,'Fixed Payload'),
			(800,'Variable Payload'),
	)

	#Relations
	vessel_id = models.ForeignKey(VESSEL, on_delete=models.CASCADE,verbose_name='Vessel',related_name="items")
	#Attributes - Mandatory
	id = models.AutoField(primary_key=True)
	part_name = models.CharField('Part Name', max_length=32,blank=False)
	group_system = models.PositiveSmallIntegerField('Group System',choices=GROUP_SYSTEM_CHOICE,default=100)
	description = models.TextField(blank=True)
	quantity = models.PositiveSmallIntegerField('Quantity',null=True,default=1)
	####################### MASS PROPERTIES FROM ABSTRACT CLASS  #################################

	#Attributes - Optional
	#Object Manager
	#Custom Properties

	#Dunders
	def __str__(self):
		return '{:s} in group system {:d}'.format(self.part_name,self.group_system)

	def __repr__(self):
		return '{:s}'.format(self.part_name)

	#Methods


	#Meta
	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Items'
		ordering = ['group_system','-mass']
		#unique_together = (vessel_id,)