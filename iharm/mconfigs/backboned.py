from .base import BMCONFIGS
from iharm.model.backboned import DeepLabIHModel, HRNetIHModel


MCONFIGS = {
    'hrnet18s_idih256': {
        'model': HRNetIHModel,
        'params': {'base_config': BMCONFIGS['improved_dih256']}
    },
    'hrnet18s_v2p_idih256': {
        'model': HRNetIHModel,
        'params': {'base_config': BMCONFIGS['improved_dih256'], 'pyramid_channels': 256}
    },
    'hrnet18_idih256': {
        'model': HRNetIHModel,
        'params': {'base_config': BMCONFIGS['improved_dih256'], 'small': False}
    },
    'deeplab_r34_idih256': {
        'model': DeepLabIHModel,
        'params': {'base_config': BMCONFIGS['improved_dih256']}
    },
    'hrnet18_idih512': {
        'model': HRNetIHModel,
        'params': {'base_config': BMCONFIGS['improved_dih512'], 'small': False, 'downsize_hrnet_input': True}
    },
    'hrnet18_sedih512': {
        'model': HRNetIHModel,
        'params': {'base_config': BMCONFIGS['improved_sedih512'], 'small': False, 'downsize_hrnet_input': True}
    }
}
