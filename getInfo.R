#Helper function for reading in file data
library("poweRlaw")
analyze_data <- function(data_file, name, iters){
		
    	fileConn <- file(name, open='a')
    	data <- read.csv(file=data_file, sep=",", colClasses=c("NULL", NA), header=F)
    	data <- data[,1]
    	m_pl = displ$new(data)
    	est = estimate_xmin(m_pl)
    	m_pl$setXmin(est)

    	print("m_pl fit")
    	print(m_pl)

    	bs_p = bootstrap_p(m_pl, threads = 6, no_of_sims = iters)
    	print("***************************")
    	print("bootstrap results")
    	print(bs_p)
	print(bs_p$p)
	write(c('bootstrap p-value:',bs_p$p), fileConn)

}

compare_dist <- function(data_file, name, iters){
	

	fileConn <- file(name, open='a')
    	data <- read.csv(file=data_file, sep=",", colClasses=c("NULL", NA), header=F)
    	data <- data[,1]
    	m_pl = displ$new(data)
    	m_pl$setXmin(estimate_xmin(m_pl))

	m2 = dislnorm$new(data)
	m2$setXmin(m_pl$getXmin())
	m2$setPars(estimate_pars(m2))

	m3 = dispois$new(data)
	m3$setXmin(m_pl$getXmin())
	m3$setPars(estimate_pars(m3))

	m4 = disexp$new(data)
	m4$setXmin(m_pl$getXmin())
	m4$setPars(estimate_pars(m4))

	comp_lnorm = compare_distributions(m_pl,m2)
	comp_pois = compare_distributions(m_pl,m3)
	comp_exp = compare_distributions(m_pl,m4)

	print("Lnorm")
	print(comp_lnorm$p_two_sided)
	print(comp_lnorm$test_statistic)
	write(c("Lnorm:",cat('p:',comp_lnorm$p_two_sided),cat('q:',comp_lnorm$test_statistic)),fileConn,append=TRUE, sep="\n\n")

	print("Pois")
	print(comp_pois$p_two_sided)
	print(comp_pois$test_statistic)
	write(c("Lnorm:",cat('p:',comp_pois$p_two_sided),cat('q:',comp_pois$test_statistic)),fileConn,append=TRUE, sep="\n\n")


	print("Exp")
	print(comp_exp$p_two_sided)
	print(comp_exp$test_statistic)
	write(c("Lnorm:",cat('p:',comp_exp$p_two_sided),cat('q:',comp_exp$test_statistic)),fileConn,append=TRUE, sep="\n\n")
}

get_info <- function(data_file, name, iters){
	
	fileConn <- file(name, open='a')
    	data <- read.csv(file=data_file, sep=",", colClasses=c("NULL", NA), header=F)
    	data <- data[,1]
    	m_pl = displ$new(data)
    	est = estimate_xmin(m_pl)
    	m_pl$setXmin(est)

	write(c("Xmax:",data[1]),fileConn)
    	print("Xmax")
	print(data[1])

	write(c("Xmin:",est$xmin),fileConn,append=TRUE, sep="\n\n")
	print("Xmin")
	print(est)
	
	write(c("Word count:",sum(data)),fileConn,append=TRUE, sep="\n\n")
	print("Word count")
	print(sum(data))
}


current_data <- readline(prompt="Data_file_name: ")
results_file <- readline(prompt="Results_file_name: ")
get_info(current_data,results_file)
print('next')
analyze_data(current_data, results_file, 5000)
print('next')
compare_dist(current_data, results_file)


