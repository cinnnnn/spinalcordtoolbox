# helper module to expose cli scripts outside top-level package

import os
import sys

from spinalcordtoolbox import __sct_dir__

# add scripts location to path
sys.path.append(os.path.join(__sct_dir__, 'scripts'))

# import all scripts
import sct_analyze_lesion
import sct_analyze_texture
import sct_apply_transfo
import sct_check_dependencies
import sct_compute_ernst_angle
import sct_compute_hausdorff_distance
import sct_compute_mscc
import sct_compute_mtr
import sct_compute_mtsat
import sct_compute_snr
import sct_convert
import sct_create_mask
import sct_crop_image
import sct_deepseg_gm
import sct_deepseg_lesion
import sct_deepseg
import sct_deepseg_sc
import sct_denoising_onlm
import sct_detect_pmj
import sct_dice_coefficient
import sct_dmri_compute_bvalue
import sct_dmri_compute_dti
import sct_dmri_concat_b0_and_dwi
import sct_dmri_concat_bvals
import sct_dmri_concat_bvecs
import sct_dmri_display_bvecs
import sct_dmri_moco
import sct_dmri_separate_b0_and_dwi
import sct_dmri_transpose_bvecs
import sct_download_data
import sct_extract_metric
import sct_flatten_sagittal
import sct_fmri_compute_tsnr
import sct_fmri_moco
import sct_get_centerline
import sct_image
import sct_label_utils
import sct_label_vertebrae
import sct_maths
import sct_merge_images
import sct_process_segmentation
import sct_propseg
import sct_qc
import sct_register_multimodal
import sct_register_to_template
import sct_resample
import sct_run_batch
import sct_smooth_spinalcord
import sct_straighten_spinalcord
import sct_testing
import sct_version
import sct_warp_template