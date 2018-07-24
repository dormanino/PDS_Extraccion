import os
import LatestFileVersion


class DataPoint:

    current_working_directory = os.getcwd()
    data_12mpp = LatestFileVersion.latest_file_version('json', '12mpp_raw', current=current_working_directory + '\\DataPoint')
    data_b3902v = LatestFileVersion.latest_file_version('json', '_final_variant_data', current=current_working_directory + '\\DataPoint')
    data_12mpp_parsed = LatestFileVersion.latest_file_version('json', '12mpp_parsed', current=current_working_directory + '\\DataPoint')
