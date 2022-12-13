from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser)
# Create your models here.

# class UserModel(models.Model):
#     company_name =models.CharField(max_length=35,null=False,blank=False)
#     company_startdate = models.DateField(null=True,blank=True)
#     company_bio = models.TextField
#     # routes= models.ForeignKey(max_length=50,null=True,blank=True)
#     phone_number = models.PhoneNumberField()
#     city = models.CharField(max_length=30,null=True,blank=False)
#     adhar_number = models.CharField(max_length=50)
#     gst_number = models.CharField(max_length=50)
#     is_varified = models.BooleanField(default=False)
#     is_bank_varified = models.BooleanField(default=False)
#     is_bussiness_card = models.BooleanField(default=False)

# class Role(models.Model):
#     name=models.CharField(max_length=60)

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name=models.CharField(max_length=55)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=17,verbose_name='phone number',null=True, blank=True,unique=True) # Validators should be a list
    otp= models.CharField(max_length=9, blank = True, null=True)
    referral_code=models.CharField(max_length=20,blank=True,null=True)
    otp_genarate_time=models.DateTimeField()
    is_phone_verified=models.BooleanField(
        max_length=20,default=False,help_text="Users mobile number is verfied with otp")
    is_user_verified=models.BooleanField(
        max_length=20,default=False,help_text="Aadhar and gst verified user")
    is_bank_varified=models.BooleanField(
        max_length=20,default=False,help_text="User Added his account details")
    is_busssiness_card=models.BooleanField(
        max_length=20,default=False,help_text="User created business card")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(auto_now_add=True, null=False)
    updated_timestamp = models.DateTimeField(auto_now=True, null=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email
    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Routes(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    name=models.ManyToManyField('User', related_name='authors', blank=True)
    
    def __str__(self):
        return str(self.name)
#profile section 
class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    company_start_date= models.PositiveSmallIntegerField(
        blank=True, null=True,help_text="Starting year of company"
        )
    company_bio=models.TextField()
    city=models.CharField(max_length=40,null=True,blank=True)
    routes=models.ForeignKey(Routes, on_delete=models.CASCADE, blank=True, default=None)
    profile_image=models.ImageField(upload_to='profile_images', blank=True, null=True)
    cover_images=models.ImageField(upload_to='cover_images',blank=True)


class Businesscard(models.Model):
    contact_person_name = models.CharField(max_length=30,null=False,blank=False)
    Designation =models.CharField(max_length=30,null=False,blank=False)
    Alternative_contact =models.CharField(max_length=30,null=True,blank=True)
    Email =models.EmailField(null=True,blank=True)
    Logo =models.ImageField(null=True,blank=True)
    Bussiness_Address=models.TextField(null=False,blank=False)

class Vehicalmodel(models.Model):
    Vehicle_name =models.CharField(max_length=30,null=False,blank=False)
    Vehicle_load_capacity=models.CharField(max_length=30,null=False,blank=False)
    Vehicle_Type=models.CharField(max_length=30,null=False,blank=False)
    Is_Tyres_defined=models.BooleanField(null=True,blank=True,default=False)



class Attachnewlorry(models.Model):
    UserVehicle_number=models.CharField(max_length=50,null=False,blank=False)
    Current_location=models.CharField(max_length=35,null=False,blank=False)
    Permit=models.CharField(max_length=50)
    Is_all_permit=models.BooleanField(null=True,blank=True)
    Vehicle=models.ForeignKey(Vehicalmodel, on_delete=models.CASCADE)
    Is_active=models.BooleanField(null=True,blank=True,default=True)
    Is_Rc_verfied=models.BooleanField(null=True,blank=True,default=False)

class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
def __str__(self):
        return str(self.Mobile)