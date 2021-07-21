library('rvest')
library('tidyverse')
library('janitor')
library('ggplot2')
library('dplyr')

library('stringr')
content <- read_html('https://www.weatherzone.com.au/nsw/sydney/sydney/detailed-forecast')
content[is.na(content)] = 0

tables <- content %>% html_table(fill = TRUE)
first_table <- tables[[1]]
#first_table<-subset(first_table, DF$first_table...1.!=DF$first_table...4.)
first_table$Weather<- str_sub(first_table$Weather,0,-3)
first_table$Temp<-str_sub(first_table$Temp,0,-3)
first_table$`Dew point`<-str_sub(first_table$`Dew point`,0,-3)
first_table$`Chance of rain`<- str_sub(first_table$`Chance of rain`,0,-2)
first_table$`Cloud cover` <- str_sub(first_table$`Cloud cover` ,0,-2)
#first_table$Wind.1 <- str_sub(first_table$Wind.1 ,0,-5)
#first_table$Wind.1 <- str_sub(first_table$Wind.1 , -3,)
first_table$Humidity <- str_sub(first_table$Humidity ,0,-2)



DF<-data.frame(first_table[,1],first_table[,4],first_table[,5], first_table[,6], first_table[,8],first_table[,9],first_table[,10])

DF<-DF[!grepl("Monday,", DF$first_table...1.),]
DF<-DF[!grepl("Tuesday,", DF$first_table...1.),]
DF<-DF[!grepl("Wednesday,", DF$first_table...1.),]
DF<-DF[!grepl("Thursday,", DF$first_table...1.),]
DF<-DF[!grepl("Friday,", DF$first_table...1.),]
DF<-DF[!grepl("Satday,", DF$first_table...1.),]
DF<-DF[!grepl("Sunday,", DF$first_table...1.),]
#print(DF)
colnames(DF) <- c("Time", "Temp", "Chance of Rain", "Cloud Cover", "Wind", "Dew Point", "Humidity")
DF<- DF(0,-5)
write.csv(DF,"https:\\github.com\\benbowen267\\WeatherKnowledge\\blob\\master\\my_data.csv", row.names = FALSE)



#par(mar = c(6.5, 6.5, 2, 8), mgp = c(5, 1, 0))
#x<- 1:13
#y1<- DF$first_table...4.[1:13] #temp
#y2<- DF$first_table...5.[1:13] #chanceofrain
#y3<- DF$first_table...6.[1:13] #cloudcover
#y4<- DF$first_table...8.[1:13] #wind
#y5<- DF$first_table...9.[1:13] #dewpoint
#y6<- DF$first_table...10.[1:13] #humidity


#plot(x, y1, 'l',
    # main = "Temp and Humidity next 45 Hours",
#xlab = "<<   THE NEXT 45 HOURS    >>",
#ylab = "TEMPERATURES",
#ylim=c(5,45), lwd=2,
#xaxt= 'n')

#par(new=T)
#plot(x, y2, axes=F, ylim=c(0, 100), xlab="", ylab="", 
 #    type="l",lty=1, main="",xlim=c(1,13),lwd=2, col= "red")
#legend('top',                                       
#       legend= c("Chance of Rain", "Cloud Cover"),
#       col = c("red", "blue"),
#       lty = 1,
#       horiz=TRUE, cex=0.5)
#par(new=T)
#plot(x, y3, axes=F, ylim=c(0, 100), xlab="", ylab="", 
#     type="l",lty=1, main="Chane of Rain next 45 Hours",xlim=c(1,13),lwd=2, col= "blue")

#axis(side= 4, ylim=c(0,100),twd=1, col="BLACK",lwd.ticks = 1, tck = 0.02,cex.main=1, cex.lab=1, cex.axis=1,
#     mtext("Chance of Rain, Cloud Cover", las= 3, side= 4, line=2.5, cex.label=1, col="black"))
#par(new=T)
#plot(x, y4, axes=F, ylim=c(5, 45), xlab="", ylab="", 
    # type="l",lty=1, main="",xlim=c(1,13),lwd=2, col= "purple")

#par(new=T)
#plot(x, y6, axes=F, ylim=c(0, 100), xlab="", ylab="", 
#     type="l",lty=1, main="",xlim=c(1,13),lwd=2, col= "orange")

#axis(1, 1:17, DF$first_table...1., col.axis="black")





