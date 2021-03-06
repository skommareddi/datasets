# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for tensorflow_datasets.core.features.video_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import features
from tensorflow_datasets.core import test_utils

tf.compat.v1.enable_eager_execution()


class VideoFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):

    np_video = np.random.randint(256, size=(128, 64, 64, 3), dtype=np.uint8)

    return [
        test_utils.FeatureExpectation(
            name='video',
            feature=features.Video(shape=(None, 64, 64, 3)),
            shape=(None, 64, 64, 3),
            dtype=tf.uint8,
            tests=[
                # Numpy array
                test_utils.FeatureExpectationItem(
                    value=np_video,
                    expected=np_video,
                ),
                # File path (Gif)
                # File path (.mp4)
            ],
        ),
    ]


if __name__ == '__main__':
  test_utils.main()
