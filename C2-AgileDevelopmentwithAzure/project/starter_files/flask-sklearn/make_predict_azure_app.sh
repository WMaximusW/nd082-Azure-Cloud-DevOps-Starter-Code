#!/usr/bin/env bash

PORT=443
echo "Port: $PORT"

# POST method predict
curl -d '{
   "CHAS": {
      "0": 0
   },
   "RM": {
      "0": 6.575
   },
   "TAX": {
      "0": 296.0
   },
   "PTRATIO": {
      "0": 15.3
   },
   "B": {
      "0": 396.9
   },
   "LSTAT": {
      "0": 4.98
   }
}' \
-H "Content-Type: application/json" \
-X POST "https://trungnq72-project2-fubufxbgb7hab7e0.eastus-01.azurewebsites.net/predict" \
-v  # This makes curl verbose and shows what's happening

# Prevent the script from closing
read -p "Press any key to exit..."
