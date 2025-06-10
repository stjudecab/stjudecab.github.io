# St. Jude Center for Applied Bioinformatics(CAB)

Our website is based on [jekyll](https://jekyllrb.com)
- The open source templates were forked from [Dr. Stephan Sanders](https://github.com/sanderslab/sanderslab.github.io),
- Earlier version designed and shared by the labs of [Dr. Allan Drummond](http://www.allanlab.org/aboutwebsite.html) and [Trevor Bedford](http://bedford.io/misc/about/)
- [Full Publication list](https://alshedivat.github.io/al-folio/publications/) using al-folio adapt from [Maruan Al-Shedivat](https://github.com/alshedivat/al-folio) based on jekyll plugin [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar)
- We greatful thank them for sharing code and knowledge.
- We added plugin [jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship) to improve table shown by markdown.
- Check **[script/README.md](script/)** for more customization


If you use conda, these will help you start build for your own
- Step1: Fork [https://github.com/stjudecab/stjudecab.github.io](https://github.com/stjudecab/stjudecab.github.io)
- Step2: on you forked git, click setting and get your own repository name
- Step3: Under linux
```
git clone https://github.com/**yourid**/stjudecab.github.io
#conda create -n iobuild python=3.8 ruby=2.6.3
#conda activate iobuild
conda env create -f .condaenv.yml -n iobuild
export CONDA_BUILD=1
conda activate iobuild
gem install bundle
bundle install
#local debug, would rebuild automatically everytime you changed a file
yourip=$(hostname -I | awk '{printf $1}')
bundle exec jekyll serve --host $yourip --port 5050 --livereload
#after confirmation of the changes you want
bundle exec jekyll build
git commit "update" && git push
sh script/deploy
#Note it might take a few minutes for github.io to update, be patient
```


The website is deployed using [GitHub Pages](https://stjudecab.github.io) and the source code is available on [GitHub](https://github.com/stjudecab/stjudecab.github.io). Please feel free to reuse this code (making sure to cite the Maruan, Sanders, Bedford and Drummond lab as the original sources of the lab website template).
