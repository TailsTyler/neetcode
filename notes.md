command to make file names
1. i=1; for name in "Valid Parentheses" "Min Stack" "Evaluate Reverse Polish Notation" "Generate Parentheses" "Daily Temperatures" "Car Fleet" "Largest Rectangle In Histogram"; do printf -v num "%02d" $i; touch "${num}_$(echo "$name" | tr ' ' '_').py"; ((i++)); done
