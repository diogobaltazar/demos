from bellman_ford_variation_1 import shortest_paths, build_table
from pydash import py_
import json
import networkx as nx
import matplotlib
import functools as f
import csv




# COLS = [
#     'from_code',
#     'to_code',
#     'from_location',
#     'to_location',
#     'from_city',
#     'to_city',
#     'from_country',
#     'to_country',
#     'from_zip_code',
#     'to_zip_code',
#     'from_type',
#     'to_type',
#     'from_lon',
#     'from_lat',
#     'to_lon',
#     'to_lat',
#     'loc',
#     'rate_valid_from',
#     'rate_valid_to',
#     'full_empty',
#     'customer_nominated',
#     'distance_band_min',
#     'distance_band_max',
#     'distance',
#     'supplier_name',
#     'customer_name',
#     'modality',
#     'modality_group',
#     'contract_id',
#     'contract_name',
#     'market',
#     'payment_terms',
#     'rate_type',
#     'area',
#     'bid_load_date',
#     'directionex_im_pos',
#     'currency',
#     'corridor_code',
#     'container_type',
#     'is_reefer',
#     'container_size',
#     'rate_category',
#     'weight_bandsgross_tonmin',
#     'weight_bandsgross_tonmax',
#     'sap_vendor_code',
#     'flex_id',
#     'delivery_mode',
#     'item_type',
#     'item_name',
#     'subject_to_fuel',
#     'road_tollsabsolute',
#     'tcoexcl_vas',
#     'fuel_surcharge_comments',
#     'surcharge_description',
#     'surcharge_rate',
#     'fuel_surcharge',
#     'basic_rate'
# ]

# col = lambda _: COLS.index(_)

# K = dict()

# with open('/home/diogo/Downloads/coupa_foundry_extract_full_12052020.csv', newline='') as data:
#     data = csv.reader(data, delimiter=',')
#     for row in data:
#         origin      = row[col('from_location')]
#         destination = row[col('to_location')]
#         encode      = row[col('container_size')]

#         (
#             K
#             .setdefault(origin,         {})
#             .setdefault(destination,    {})
#             .setdefault(encode,         [])
#         )
        
#         K[origin][destination][encode].append({
#             'supplier_name'     : row[col('supplier_name')],
#             'basic_rate'        : row[col('basic_rate')],
#             'modality'          : row[col('modality')],
#             'rate_type'         : row[col('rate_type')],
#             'rate_valid_from'   : row[col('rate_valid_from')],
#             'rate_valid_to'     : row[col('rate_valid_to')]
#         })


# print(json.dumps(K, indent = 4, sort_keys = True))
    





# # G = {
# #     'a': [
# #         {'destination': 'b', 'size': 1, 'type': 1, 'height': 1, 'rate': 1 },
# #         {'destination': 'c', 'size': 1, 'type': 1, 'height': 1, 'rate': 2 }],
# #     'b': [
# #         {'destination': 'c', 'size': 1, 'type': 1, 'height': 1, 'rate': 2},
# #         {'destination': 'd', 'size': 1, 'type': 1, 'height': 1, 'rate': 10}],
# #     'c': [
# #         {'destination': 'd', 'size': 1, 'type': 1, 'height': 1, 'rate': 2},
# #         {'destination': 'e', 'size': 1, 'type': 1, 'height': 1, 'rate': 1}],
# #     'd': [],
# #     'e': [
# #         {'destination': 'd', 'size': 1, 'type': 1, 'height': 1, 'rate': 1}],
# #     'g': [
# #         {'destination': 'c', 'size': 1, 'type': 1, 'height': 1, 'rate': 1}],
# # }

# # pre-process: rate validity overlapping + vendor.rate ordering
# # after-process: top N + validity

G = {
    'a': {
        'b': [
            { 'encode': '111', 'vendor':  [ # edge attributes: size: 1, type 1, height: 1, vendor
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
        'c': [
            { 'encode': '111', 'vendor':  [ # size: 1, type 1, height: 1
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
    },
    'b': {
        'c': [
            { 'encode': '111', 'vendor':  [ # size: 1, type 1, height: 1
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
        'd': [
            { 'encode': '111', 'vendor':  [ # size: 1, type 1, height: 1
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
    },
    'c': {
        'd': [
            { 'encode': '111', 'vendor':  [ # size: 1, type 1, height: 1
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
    },
    'd': {
        'c': [
            { 'encode': '111', 'vendor':  [ # size: 1, type 1, height: 1
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            { 'encode': '121', 'vendor':  [
                {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
                {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            ]},
            # { 'encode': '131', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '211', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '221', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '231', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '311', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '312', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
            # { 'encode': '313', 'vendor':  [
            #     {'name': 'X1', 'rate': 1, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X2', 'rate': 2, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X3', 'rate': 3, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X4', 'rate': 4, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X5', 'rate': 5, 'modality': 'truck', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            #     {'name': 'X6', 'rate': 6, 'modality': 'train', 'rate_type': 1, 'validity_from': '2020-02-02', 'validity_to': '2020-12-02' },
            # ]},
        ],
    },
}

# N = 3



# # H = shortest_paths(G, 3)
# # n = py_.map(H['c'], lambda _: {list(_)[0]: list(_.values())[0]} )
# # print(
# #     H
# # )

# encodes = [
#     '111', '121', '131',
#     '211', '221', '231',
#     '311', '312', '313',
# ]

H = {
    'a': {
        'b':[ 
            {'encode': '111', 'vendor': [
                {'rate': 1}
            ]},
            {'encode': '112', 'vendor': [
                {'rate': 1}
            ]},
        ],
        'c': [ 
            {'encode': '111', 'vendor': [
                {'rate': 5}
            ]},
            {'encode': '112', 'vendor': [
                {'rate': 5}
            ]},
        ]
    },
    'b': {
        'c': [ 
            {'encode': '111', 'vendor': [
                {'rate': 3}
            ]},
            {'encode': '112', 'vendor': [
                {'rate': 3}
            ]},
        ],
        'd': [ 
            {'encode': '111', 'vendor': [
                {'rate': 1}
            ]},
            {'encode': '112', 'vendor': [
                {'rate': 1}
            ]},
        ]
    },
    'd': {
        'c': [ 
            {'encode': '111', 'vendor': [
                {'rate': 1}
            ]},
            {'encode': '112', 'vendor': [
                {'rate': 1}
            ]},
        ]
    },
}

# user inputs
ORIG = 'a'
DEST = 'b'
N = 1
VALID_DT = '2020-02-02'
VERBOSE = False
encode = '111'
G_STAR = nx.MultiDiGraph()
MAX_CONTAINER_CHANGE = None

# populate networkx
# requires:
# R1 - vendor list is sorted
# R2 - validity dates have been intersected
for orig in G:
    if VERBOSE: print(orig)

    for dest in G[orig]:
        if VERBOSE: print("|- %s" %(dest))
        G_STAR.add_edge( orig, dest )

print('> get paths')
for path in nx.all_simple_paths(G_STAR, 'a', 'c'):
    print(path)

paths = dict()
for path in nx.all_simple_paths(G_STAR, 'a', 'c'):
    res = []
    for i in range(len(path) - 1):
        res.append(path[i] + path[i+1])
    # paths[''.join(path)] = [G[_[0]][_[1]] for _ in ['ab', 'bd', 'dc']]
    print(res)

# print(json.dumps(paths, sort_keys=True, indent=4))

# print(
#     list(filter(lambda _: _['encode'] == encode, G['a']['b']))[0]['vendor'][0:N]
# )
        





# # print([H[_[0]][_[1]] for _ in ['ab', 'bd', 'dc']])
# # print(f.reduce(lambda x, y: x + y, [H[_[0]][_[1]] for _ in ['ab', 'bd', 'dc']]))



# # for u, v in G_STAR.edges('a'):
# #     print(u, v)
# # print([v for u,v in G_STAR.edges('a')])