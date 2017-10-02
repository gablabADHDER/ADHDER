function [ Score, Results ] = ReadWMLocData( Data, inputFile )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

% inputFile = '/Volumes/cristae/samadhi_daeda/coding/ADHD_EmotionRegulation/WMLocalizer/data/Data_P1_2016_Dec_18_1912.txt';

% load subject ID

% set up results structure
for iBlock = 1:2:8
    Results{iBlock}.expType = '2-back';
end
for iBlock = 2:2:8
    Results{iBlock}.expType = '0-back';
end

% read output file into data table
T = readtable(inputFile, 'Delimiter', '\t', 'ReadVariableNames', true);

% turn data into number array (remove target letter)
tempData = table2array(T(:,[1:2,4:end]));

% get the block numbers
blocks = unique(tempData(:,1));

% reformat into cells
for iBlock = 1:length(blocks)
    Results{iBlock}.data = tempData(tempData(:,1) == blocks(iBlock),3:end);
end

% calculate hits and misses
for iBlock = 1:length(Results)
    tempHits = (Results{iBlock}.data(:,1) == 1) .* (Results{iBlock}.data(:,2) == 1);
    Results{iBlock}.hitsCorrect = sum(tempHits);
    tempMissedHits = (Results{iBlock}.data(:,1) == 1) .* (Results{iBlock}.data(:,2) ~= 1);
    Results{iBlock}.missedTargets = sum(tempMissedHits);
    tempFalsePositives = (Results{iBlock}.data(:,1) == 0) .* Results{iBlock}.data(:,2) == 1;
    Results{iBlock}.falsePositives = sum(tempFalsePositives);
    Results{iBlock}.totalTrials = length(Results{iBlock}.data(:,1));
    clearvars tempHits tempMissedHits tempFalsePositives
end

Score{1}.exp2back = [];
Score{1}.exp0back = [];
Score{1}.key = {'hits','misses','false positives','total trials'};

ii = 0;
jj = 0;
for iBlock = 1:length(Results)
    if strcmp(Results{iBlock}.expType, '2-back')
        ii = ii + 1;
        Score{1}.exp2back(ii,:) = [Results{iBlock}.hitsCorrect, Results{iBlock}.missedTargets, Results{iBlock}.falsePositives, Results{iBlock}.totalTrials];
    elseif strcmp(Results{iBlock}.expType, '0-back')
        jj = jj + 1;
        Score{1}.exp0back(jj,:) = [Results{iBlock}.hitsCorrect, Results{iBlock}.missedTargets, Results{iBlock}.falsePositives, Results{iBlock}.totalTrials];
    else
        error('unrecognized')
    end
end