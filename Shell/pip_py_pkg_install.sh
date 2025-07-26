#!/bin/bash
exec > ./Shell/pip_py_pkg_install_script_output.log 2>&1

echo -e "*** Installing Pandas ***\n"
pip3 install pandas

echo -e "\n*** Installing Matplotlib ***\n"
pip3 install matplotlib

echo -e "\n*** Installing Seaborn ***\n"
pip3 install seaborn

echo -e "\n*** Installing Plotly ***\n"
pip3 install plotly