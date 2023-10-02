## author: xin luo
## create: 2021.10.27, modify: 2023.10.1


import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix


## --------- conventional image-based -------- ##
## usually used for accuracy assessment of image classificaiton 
def acc_matrix(cla_map, truth_map=None, sam_pixel=None, id_label=None):
    ''' 
    des: calculate the accuracy matrix
    args: 
        cla_map: classification result of the full image.
        truth_map: truth image (either truth_map or sam_pixel should be given).
        sam_pixel: np.array, (num_samples,3), col 1,2,3 are the row,col and label.            
        id_label: 0/1/2/..., Calculating producer's or user's accuracy for target class.
    Note: Either one of the truth_map and sam_pixel should be determination. 
    Return: 
        acc_oa, confus_mat: the overall accuracy and confusion matrix
    '''
    if sam_pixel is not None:
        sam_result = []
        sam_label = sam_pixel[:,2]
        num_cla = sam_label.max()+1
        labels = list(range(num_cla))
        for i in range(sam_label.shape[0]):
            sam_result.append(cla_map[sam_pixel[i,0], sam_pixel[i,1]])            
        sam_result = np.array(sam_result)
    if truth_map is not None:
        sam_label = truth_map.flatten()  
        sam_result = cla_map.flatten()
        num_cla = sam_label.max()+1
        labels = list(range(num_cla))
    acc_oa = np.around(accuracy_score(sam_label, sam_result), 4)
    confus_mat = confusion_matrix(sam_label, sam_result, labels=labels)
    if id_label is not None:
        acc_prod=np.around(confus_mat[id_label, id_label]/confus_mat[id_label,:].sum(), 4)
        acc_user=np.around(confus_mat[id_label, id_label]/confus_mat[:,id_label].sum(), 4)
        return acc_oa, acc_prod, acc_user, confus_mat
    else:
        return acc_oa, confus_mat

def acc_miou(cla_map, truth_map, labels=None):
    '''
    des: calculate the mean IoU metric.
    args:
        cla_map: classification result of the full image
        truth_map: truth image (either truth_map or sam_pixel should be given)
        labels: a list, the class id for calculating. e.g., [0,1,2]
    return:
        MIoU score
    '''  
    iou = []
    if labels == None:
        labels = np.unique(truth_map)
    for label in labels:
        intersection = np.logical_and(cla_map==label, truth_map==label)
        union = np.logical_or(cla_map==label, truth_map==label)
        iou_score = np.sum(intersection)/np.sum(union)
        iou.append(iou_score)
    return np.mean(iou)

