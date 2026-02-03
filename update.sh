
#echo "Building services.json"
#python scripts/build_services.py

#echo "Running Services Script"
#python scripts/service_list_generator.py


#echo "Custom Cats"
#./scripts/build_categories.sh

echo "Run Generator"
pyton scripts/generator.py
echo "Running Tunneling Script"
python scripts/tunneling.py
