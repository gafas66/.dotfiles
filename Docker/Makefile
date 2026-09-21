################################################################################
# Created: Monday, September 21 2026
# Author: , ESK
.ONESHELL:

CM = CMakeLists.txt

player:
	git clone https://github.com/playerproject/player.git
	export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
	cd player
	sed -i '1s/^/set (CMAKE_CXX_STANDARD_REQUIRED ON)\n/' ${CM}
	sed -i '1s/^/set (CMAKE_CXX_STANDARD 11)\n/'          ${CM}
	mkdir build
	cd build
	cmake ../
	make
	sudo make install
	echo 'export PATH=${PATH}:/usr/local/bin' >> ~/.bashrc
	echo 'export PLAYERPATH="/usr/local/lib"' >> ~/.bashrc
	echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib' >> ~/.bashrc

stage:
	git clone https://github.com/rtv/Stage.git
	export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
	export STG=$HOME/stg
	cd Stage
	sed -i '1s/^/target_include_directories (/usr/local/ntirpc)\n/' ${CM}	
	mkdir build;cd build
	cmake -DCMAKE_INSTALL_PREFIX=${STG} ../
	make
	sudo make install

build:; sudo docker build -t playerstage -f PlayerStage .
#build:; sudo docker build -t playerstage -f AIPlayerStage .
start:
	-sudo docker rm -f test1
	sudo docker run -td -p 2225:22 \
	--name test1 \
	-v /home/demo_10g:/home/demo_10g \
	playerstage

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
