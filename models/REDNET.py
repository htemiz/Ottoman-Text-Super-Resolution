# EXPLANATIONS
"""
ARTICLE:
    Mao, Xiaojiao, Chunhua Shen, and Yu-Bin Yang. \
    "Image restoration using very deep convolutional encoder-decoder networks with symmetric skip connections." \
    Advances in neural information processing systems. 2016.
    
    https://arxiv.org/pdf/1603.09056.pdf

 
PARAMETERS:
    number of layer filters 64 in the paper
    optimizer: ADAM with learning rate 1e-4 
    number of filters: 64 (authors say higher values leads to slightly better performance)
    activation is relu
"""


from keras import metrics
from keras import losses
from keras.models import Model
from keras.layers import concatenate as merge
from keras.layers import Input,  ZeroPadding2D,  LocallyConnected2D, Conv2DTranspose, concatenate, BatchNormalization, Add
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.convolutional import Conv2D, UpSampling2D
from keras.layers.pooling import AveragePooling2D, GlobalAveragePooling2D, MaxPooling2D
# from keras.layers.normalization import BatchNormalization
from keras.layers import BatchNormalization
import keras.backend as K
from os.path import  dirname, abspath, basename
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from keras.layers import PReLU, LeakyReLU, ReLU

eps = 1.1e-6

settings = \
{
"activation":"relu",
'augment':[], # must be any or all lof [90,180,270, 'flipud', 'fliplr', 'flipudlr' ]
'backend': 'tensorflow',
'batchsize':256,
'channels':3,
'colormode':'RGB', # 'YCbCr' or 'RGB'
'crop': 0,
'crop_test': 6,
'decay':1e-6,
'decimation': 'bicubic',
'espatience' : 25,
'epoch':25,
'inputsize':50, #
'interp_compare': 'lanczos',
'interp_up': 'bicubic',
'lrate':1e-4,
'lrpatience': 10,
'lrfactor' : 0.5,
'metrics': ["PSNR"],
'minimumlrate' : 1e-7,
'modelname':basename(__file__).split('.')[0],
'noise':'',
'normalization':['divide', '255.0'], # ['standard', "53.28741141", "40.73203139"],
'normalizeback': False,
'normalizeground':False,
'outputdir':'',
'scale':2,
'seed': 19,
'shuffle' : True,
'stride':18, 
'target_channels': 3,
'target_cmode' : 'RGB',
'testpath': [r'D:\calisma\projeler\ottoman\dataset\test'],
'traindir': r"D:\calisma\projeler\ottoman\dataset\train",
'upscaleimage': True,
'valdir': r'D:\calisma\projeler\ottoman\dataset\val',
'weightpath':'',
'workingdir': '',
}

def encoder_layers(self, model, nb_filters=16, filter_size=3, nb_layers=10,
                   kernel_initializer="he_normal", padding="same", **kwargs):

    encoders=[]

    encoders.append(model)

    for i in range(nb_layers):
        encoder = Conv2D(nb_filters, (filter_size, filter_size), kernel_initializer=kernel_initializer,
                         padding=padding, name="encoder_{:02d}".format(i+1))(model)
        encoder= self.apply_activation(encoder, self.activation, None)

        encoders.append(encoder)

        model = encoder


    return model, encoders



def decoder_layers(self, model, encoders, channels=3, nb_filters=16, filter_size=3, nb_layers=10,
                   kernel_initializer="he_normal", padding="same",  **kwargs):

    n_filters = nb_filters
    # encoders.reverse()

    for i in range(nb_layers):

        if nb_layers % 2 == 1:
            subt_value = i
        else:
            subt_value = i + 1


        #the last layer must have the self.channels number of filters within it.
        if i == (nb_layers -1):
            n_filters = channels


        # for odd number of layers, we should include activation function
        if (nb_layers % 2 == 1) and (i == nb_layers-1):
            model = Conv2DTranspose(n_filters, (filter_size, filter_size), kernel_initializer=kernel_initializer,
                                    padding=padding, name="decoder_{:02d}".format(i + 1))(model)

            x = Add()([model, encoders[nb_layers - subt_value -1]])

            name = f"skip_{i + 1}_relu"

            model = self.apply_activation(x, self.activation, name)

        else:

            model = Conv2DTranspose(n_filters, (filter_size, filter_size), kernel_initializer=kernel_initializer,
                                    padding=padding, name="decoder_{:02d}".format(i + 1))(model)
            model = self.apply_activation(model, self.activation, None)

        if ((i+1) % 2) == 0:

            x = Add()([model, encoders[nb_layers - subt_value]])
            name = f"skip_{i + 1}_relu"
            model = self.apply_activation(x, self.activation, name)

    return model


def build_model(self, testmode=False):


    if testmode:
        input_size = None
    else:
        input_size = self.inputsize

    nb_layers = 15  # FOR RED30 (15 FOR encoder and 15 for decoder)
    nb_filters = 64


    input_shape = (input_size, input_size, self.channels)

    main_input = Input(shape=input_shape, name='main_input')
    model, encoders = encoder_layers(self, main_input, nb_layers=nb_layers,nb_filters=nb_filters)

    decoders=decoder_layers(self, model, encoders, nb_layers=nb_layers, nb_filters=nb_filters, channels=self.channels)

    model = Model(main_input, decoders)

    model.compile(Adam(self.lrate, self.decay), loss=losses.mean_squared_error)

    model.summary()

    return model