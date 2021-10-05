import pandas as pd

test_PLCC = 10
test_SROCC = 0.1
test_RMSE = 0.01
result_excel = 'result/test_result_tmp.xls'
result = pd.DataFrame()
result['PLCC'] = [test_PLCC]
result['SROCC'] = [test_SROCC]
result['RMSE'] = [test_RMSE]
result.to_excel(result_excel)
