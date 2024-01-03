::pytest -v -p no:logging -m 'sanity' --html=Reports\reports4.html testCases\ --browser chrome
:: <--this way you can comment
REM <-- or this way
REM pytest -v -p no:logging -m 'sanity' --html=Reports\reports4.html testCases\ --browser chrome

pytest -v -p no:logging  --html=Reports\reports4.html testCases\test_login4.py --browser chrome

