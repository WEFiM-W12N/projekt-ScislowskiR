from django.db import models


class Processing(models.Model):
    Reshape = 'Reshape'
    Grayscale = 'Grayscale'
    OneHot = 'OneHot'
    Rescale = 'Rescale'

    Choice_make = [(Reshape, 'Reshape'),
                    (Grayscale, 'Grayscale'),
                    (OneHot, 'OneHot'),
                    (Rescale, 'Rescale'),
                   ]

    type = models.CharField(
                    max_length=30,
                    choices=Choice_make,
                    default=None,
                    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name_plural = 'Processing'


class Deep_Learning(models.Model):

    Dense = 'Dense'
    Convolution = 'Convolution'
    Recurrent = 'Recurrent'
    Choice_make = [(Dense, 'Dense'),
                    (Convolution, 'Convolution'),
                    (Recurrent, 'Recurrent'),
                   ]

    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return f'{self.mode}'

    class Meta:
        verbose_name_plural = 'Deep Learning'

    objects = models.Manager()


class Operations(models.Model):


    Merge = 'Merge'
    Choice_make = [(Merge, 'Merge'),
                   ]
    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return f'{self.mode}'

    class Meta:
        verbose_name_plural = "Operations"

    objects = models.Manager()

class Public(models.Model):

    Tensorflow_Model = 'Tensorflow Model'
    Object_Detection_Model = 'Object Detection Model'
    VGG16 = 'VGG16'
    ResNet50 = 'ResNet50'
    InceptionV3 = 'InceptionV3'
    MobileNetV2 = 'MobileNetV2'
    UNet = 'UNet'
    Choice_make = [(Tensorflow_Model, 'Tensorflow Model'),
                   (Object_Detection_Model, 'Object Detection Model'),
                   (VGG16, 'VGG16'),
                   (ResNet50, 'ResNet50'),
                   (InceptionV3, 'InceptionV3'),
                   (MobileNetV2, 'MobileNetV2'),
                   (UNet, 'UNet'),
                   ]

    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return f'{self.mode}'

    class Meta:
        verbose_name_plural = 'Public'

    objects = models.Manager()


class Custom(models.Model):

    Custom = 'Custom'
    Choice_make = [(Custom, 'Custom')]

    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return f'{self.mode}'

    class Meta:
        verbose_name_plural = 'Custom'

    objects = models.Manager()

class Model(models.Model):
    """
        Fields and methods of the Game Type Class
    """
    objects = models.Manager()
    processing = models.ManyToManyField(Processing)
    deep_learning = models.ManyToManyField(Deep_Learning)
    operations = models.ForeignKey(Operations, on_delete=models.CASCADE, blank=True, null=True)
    public = models.ManyToManyField(Public)
    custom = models.ForeignKey(Custom, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    # production_year = models.SmallIntegerField(default=None)
    # description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'

    
    class Meta:
        verbose_name = "Model"

