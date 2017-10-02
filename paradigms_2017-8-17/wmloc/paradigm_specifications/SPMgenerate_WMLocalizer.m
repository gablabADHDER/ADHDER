function [ output_args ] = SPMgenerate_WMLocalizer( leaveout, randomization )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
randomization = 'a';
leaveout = 8;

% 4[prescan] + (4[ITI] + 6[instructions] + 6[countdown] + 2[fixation_pre] + (1.5[target] + 0.5[fixation])*18[presentation] )*8[blocks] + 2[logData] + 6[finalFixation] + 2[end]
totalTime =  4 + ( 4 + 6 + 6 + 2 + (1.5 + 0.5)*18 ) * 8 + 2 + 6 + 2;
Design = NaN(totalTime,3); % includes 8s prescan interval

if strcmp('a', randomization)
    two_back = 1;
    zero_back = 2;
elseif strcmp('b', randomization)
    two_back = 2;
    zero_back = 1;
else
    error('error')
end

Design(:,two_back) = [ ...
zeros(1,22),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,10)]'; % 2-back
Design(:,zero_back) = [ ...
zeros(1,22),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,18),zeros(1,18*2), ...
zeros(1,18),ones(1,18*2), ...
zeros(1,10)]'; % 0-back
Design(:,3) = [ ...
zeros(1,8),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,4),ones(1,12),zeros(1,2),zeros(1,18*2), ...
zeros(1,10)]'; % instructions


generateSPM(Design, leaveout, {'2-back','0-back','instructions'}, [1,2], sprintf('SPM_WMLoc_RandCon_%s',randomization))

end


function generateSPM(Design, leaveout, names, yonsets, saveName)

plottitle = regexprep(saveName,'_',' ');
for iCondition = 1:length(names)
    labels{iCondition} = regexprep(names{iCondition},'_',' ');
end

totalTime = size(Design,1);

if any(isnan(Design))
    error('NaN error')
end

onsets = repmat({[]},[length(names),1]);
durations = onsets;
durations_temp = repmat({[0]},[length(names),1]);
for iTime = leaveout+1:totalTime
    
    conditions = Design(iTime-1:iTime, :);
    contrast = conditions(2,:) - conditions(1,:);
    
    %     % find onsets
    %     a = find(contrast==1)
    %
    for iCondition = 1:size(contrast,2)
        switch contrast(iCondition)
            case 1
                onsets{iCondition} = [onsets{iCondition}, iTime-1-leaveout]; % onset is number of seconds preceeding the stim presentation
                durations_temp{iCondition} = 1;
            case -1
                durations{iCondition} = [durations{iCondition}, durations_temp{iCondition}];
            case 0
                durations_temp{iCondition} = durations_temp{iCondition} + 1;
            otherwise
                error('error')
        end
    end
    
end

Design_Collected = Design;
Design_Analyzed = Design;
Design_Analyzed = Design(leaveout+1:end,:);
Design(1:leaveout,:) = -1;

figure;
x=1:length(labels);
y=-1*(leaveout-1):totalTime-leaveout;
imagesc(x,y,Design);

ylabels = sort([0, onsets{yonsets}, totalTime-leaveout]);

set(gca,'Ytick',ylabels)
set(gca,'Xtick',1:length(labels),'XTickLabel',labels)
title({sprintf('Design: %s', plottitle),sprintf('DesignTime = %d, ScanTime = %d, LeftoutTime=%d', totalTime-leaveout, totalTime, leaveout)});
saveas(gcf,sprintf('%s.png', saveName));
close all;
save(sprintf('%s.mat', saveName),'names','onsets','durations','Design_Analyzed','Design_Collected');
end
