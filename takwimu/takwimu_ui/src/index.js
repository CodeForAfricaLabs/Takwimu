import React from 'react';
import ReactDOM from 'react-dom';

import withRoot from './withRoot';

import Hero from './components/Hero';
import Navigation from './components/Navigation';
import ProfileDetail from './components/ProfileDetail';
import MakingOfTakwimu from './components/MakingOfTakwimu';
import WhatCanYouDo from './components/WhatCanYouDo';
import WhereToNext from './components/WhereToNext';
import FeaturedAnalysis from './components/FeaturedAnalysis';
import AnalysisPage from './pages/AnalysisPage';
import FeaturedData from './components/FeaturedData';
import Footer from './components/Footer';
import LatestNewsStories from './components/LatestNewsStories';

const props = {
  countries: window.countries,
  profile: window.profileDataJson || {
    demographics: {},
    geography: {
      full_geoid: '',
      this: {
        square_kms: '',
        short_name: '',
        parents: []
      }
    },
    primary_releases: { active: {}, other: [] }
  }
};

const renderApp = (Component, id) => {
  const el = document.getElementById(id);
  if (el) {
    const App = withRoot(Component);

    ReactDOM.render(<App {...props} />, el);
  }
};

renderApp(Navigation, 'takwimuNavigation');
renderApp(ProfileDetail, 'takwimuProfileDetail');
renderApp(Hero, 'takwimuHero');
renderApp(FeaturedAnalysis, 'takwimuFeaturedAnalysis');
renderApp(FeaturedData, 'takwimuFeaturedData');
renderApp(WhatCanYouDo, 'takwimuWhatCanYouDo');
renderApp(MakingOfTakwimu, 'takwimuMakingOf');
renderApp(LatestNewsStories, 'takwimuLatestNewsStories');
renderApp(WhereToNext, 'takwimuWhereToNext');
renderApp(Footer, 'takwimuFooter');

renderApp(AnalysisPage, 'takwimuAnalysisPage');
